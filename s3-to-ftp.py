import ftplib
import boto3
import yaml
import tempfile
import os
import argparse
from os import listdir
from os.path import isfile, join
from datetime import date
import ssl
import re
import botocore

# Classes

class ImplicitFTP_TLS(ftplib.FTP_TLS):
    """FTP_TLS subclass that automatically wraps sockets in SSL to support implicit FTPS."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sock = None

    @property
    def sock(self):
        """Return the socket."""
        return self._sock

    @sock.setter
    def sock(self, value):
        """When modifying the socket, ensure that it is ssl wrapped."""
        if value is not None and not isinstance(value, ssl.SSLSocket):
            value = self.context.wrap_socket(value)
        self._sock = value


# Global variables

ssm_client = boto3.client('ssm')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
today = str(date.today())

# Functions

def get_arguments():
    argumentsParser = argparse.ArgumentParser(prog='s3-to-ftp',
                                              usage='%(prog)s --s3_bucket [bucket-name] --ssm_parameter [parameter name]',
                                           description='Process the files from s3 and store them in ftp servers')
    argumentsParser.add_argument('--s3_bucket_input',help='[REQUIRED] Define the s3 bucket where the files are stored: [my-bucket-name]', action='store', type=str)
    argumentsParser.add_argument('--s3_bucket_output',help='[REQUIRED] Define the s3 bucket where the processed files will be stored: [my-bucket-name]', action='store', type=str)
    argumentsParser.add_argument('--ssm_parameter',help='[REQUIRED] Define the ssm parameter store where the ftp credentials are stored: [my-paramter-store-name]', action='store', type=str)
    return argumentsParser.parse_args()


def main(s3_bucket_input, s3_bucket_output, ssm_parameter_name):
    with tempfile.TemporaryDirectory() as tmp_dir:

        logs_dir = tmp_dir + '/logs'
        os.mkdir(logs_dir)

        try:
            response = get_hosts_configs(s3_bucket_input, ssm_parameter_name, tmp_dir)

        except botocore.exceptions.ClientError as e: 
            log=str(e) + '\n' + "The hosts configuration couldn't be retrieved"
            logging(log, "NONE", logs_dir)
            push_logs_to_s3(s3_bucket_output, logs_dir)

            exit(1)
        
        ftp_keys = response['ftp_keys']
        ftp_configs = response['ftp_configs']

        for config in ftp_configs:
            
            try:
                host = config['host']
                port = config['port']
                connection_type = config['connection_type'].lower()
                base_path = config['base_path']            
                provider = config['provider']
                ftp_user = ftp_keys[provider]['user']
                ftp_pwd = ftp_keys[provider]['pass']
            except KeyError as e:
                log = str(e) + '\n' + "Some host configuration is missing. Check your hosts.yaml and the content of " + ssm_parameter_name
                logging(log, provider, logs_dir)

                continue

            ftp_files = []

            try:
                ftp_files = get_s3_objects(s3_bucket_input, provider, tmp_dir)
            
            except botocore.exceptions.ClientError as e:
                log = str(e)
                logging(log, provider, logs_dir)

                continue

            except KeyError:
                log = "there is no files from provider " + provider + " in " + s3_bucket_input + "/FILES/"
                logging(log, provider, logs_dir)

            if ftp_files:
                process_files(host, port, connection_type, base_path, ftp_user, ftp_pwd, s3_bucket_input, s3_bucket_output, ftp_files, provider, logs_dir)


        push_logs_to_s3(s3_bucket_output, logs_dir)


def get_hosts_configs(s3_bucket_input, ssm_parameter_name, tmp_dir):

    # Retrieve ftp hosts credentials
    ftp_keys = yaml.load(ssm_client.get_parameter(Name=ssm_parameter_name, WithDecryption=True)['Parameter']['Value'], yaml.SafeLoader)

    # Retrieve ftp hosts configurations
    with open(tmp_dir + '/hosts.yaml', 'wb') as data:
        s3_client.download_fileobj(s3_bucket_input, 'hosts.yaml', data)
    ftp_configs=yaml.load(open(tmp_dir + '/hosts.yaml').read(), yaml.SafeLoader)['hosts']

    return {"ftp_keys": ftp_keys, "ftp_configs": ftp_configs}


def get_s3_objects(s3_bucket_input, provider, tmp_dir):

    s3_response = s3_client.list_objects_v2(Bucket=s3_bucket_input, Delimiter='/')['Contents']

    ftp_files=[]

    for element in s3_response:

        matched_file = re.search('_'+provider, element['Key'])

        if matched_file != None:

            matched_file = re.search('.xml$', element['Key'])
        
            if matched_file != None:

                file_name = element['Key'].split("/")[-1]
                ftp_file = {"s3_key": element['Key'], "local_path": tmp_dir + '/' + file_name, "file_name": file_name}
    
                ftp_files.append(ftp_file)
    
                with open(ftp_file['local_path'], 'wb') as data:
                    s3_client.download_fileobj(s3_bucket_input, ftp_file['s3_key'], data)

    return ftp_files


def process_files(host, port, connection_type, base_path, ftp_user, ftp_pwd, s3_bucket_input, s3_bucket_output, ftp_files, provider, logs_dir):

    connected=False

    try:
        ftp = ftp_connect(host, port, connection_type, ftp_user, ftp_pwd)
        connected = True
        
    except ftplib.all_errors as e:
        log = str(e) + " host: "+ host + " port: " + str(port)
        logging(log, provider, logs_dir)

    if connected:
        for file in ftp_files:

            copy_source = {'Bucket': s3_bucket_input, 'Key': file['s3_key']}

            try:
                local_file = open(file['local_path'], 'rb')
                ftp.storbinary('STOR '+ base_path + file['file_name'], local_file)
                local_file.close()                                    # close file

                s3_resource.meta.client.copy(copy_source, s3_bucket_output, 'PROCESSED/'+ provider + '/' + today + '/' + file['file_name'])

            except ftplib.all_errors as e:
                log = str(e) + " "+ provider + '/' + file['file_name']
                logging(log, provider, logs_dir)

                s3_resource.meta.client.copy(copy_source, s3_bucket_output, 'FAILED/'+ provider + '/' + today + '/' + file['file_name'])

            except botocore.exceptions.ClientError as e: 
                log = str(e)
                logging(log, provider, logs_dir)

                continue
            
            try:
                s3_client.delete_object(Bucket=s3_bucket_input, Key=file['s3_key']) #Delete processed file
            
            except botocore.exceptions.ClientError as e: 
                log = str(e) + '\n' + 'Processed file could not be deleted after be moved to the output location'
                logging(log, provider, logs_dir)

                continue

        ftp.close() # close ftp

            

    else:
        for file in ftp_files:
            copy_source = {'Bucket': s3_bucket_input, 'Key': file['s3_key']}
            s3_resource.meta.client.copy(copy_source, s3_bucket_output, 'FAILED/'+ provider + '/' + today + '/' + file['file_name'])

            s3_client.delete_object(Bucket=s3_bucket_input, Key=file['s3_key']) #Delete processed file


def ftp_connect(host, port, connection_type, ftp_user, ftp_pwd):

    if connection_type == "tls-implicit":
        ftp = ImplicitFTP_TLS()
        ftp.connect(host=host, port=port, timeout=40)
        ftp.login(user=ftp_user, passwd=ftp_pwd)
        ftp.prot_p()
        return ftp

    elif connection_type == "tls-explicit":
        ctx = ssl._create_stdlib_context(ssl.PROTOCOL_TLSv1)
        ftp = ftplib.FTP_TLS(context=ctx)
        ftp.connect(host=host, port=port, timeout=40)
        ftp.login(user=ftp_user, passwd=ftp_pwd)
        ftp.prot_p()
        return ftp

    elif connection_type == "passive":
        ftp = ftplib.FTP()
        ftp.connect(host=host, port=port, timeout=40)
        ftp.login(user=ftp_user, passwd=ftp_pwd)
        ftp.set_pasv(True)
        return ftp

    else:
        ftp = ftplib.FTP()
        ftp.connect(host=host, port=port, timeout=40)
        ftp.login(user=ftp_user, passwd=ftp_pwd)
        ftp.set_pasv(False)
        return ftp        


def logging(log, provider, logs_dir):
    with open(logs_dir + '/' + provider + '.log', 'a') as file:
        file.write(log + '\n')


def push_logs_to_s3(s3_bucket_output, logs_dir):
    logs_files = [f for f in listdir(logs_dir) if isfile(join(logs_dir, f))]

    if logs_files:

        for file in logs_files:

            provider = file.split(".")[0]

            try:
                with open(logs_dir + '/' + file, 'rb') as data:
                    s3_client.upload_fileobj(data, s3_bucket_output, 'LOGS/' + provider + '/' + today + '/' + file)
            
            except botocore.exceptions.ClientError as e: 
                log = str(e) + '\n' + 'log ' + file + ' could not be pushed to output bucket'
                print(log)

    


args = get_arguments()
s3_bucket_input = args.s3_bucket_input
s3_bucket_output = args.s3_bucket_output
ssm_parameter_name = args.ssm_parameter

if s3_bucket_input == None or s3_bucket_output == None or ssm_parameter_name == None:

    print("[ERROR] You didn't set the parameters. Run --help for more information")
    exit(1)

else:
    main(s3_bucket_input, s3_bucket_output, ssm_parameter_name)