import os
from shutil import copyfile

class Rename():
    def __init__(self, path = r'C:\Users\Erno\Documents\"Programas Atom"\Python\Warner\"Ejemplos Softni Files"'):
        self.WATCH_PATH = "./Warner/Ejemplos Softni Files"
        self.path = path

        self.accept_pattern = ['.spa', '.por', '.eng', '.pop', '.spp', '.enp', '.SPA', '.ENG', '.POR']

        self.SPANISH_EXTENSIONS = ['.spa', '.SPA', '.spp']
        self.PORTUGUESE_EXTENSIONS = ['.por', '.POR', '.pop']
        self.ENGLISH_EXTENSIONS = ['.eng', '.ENG', '.enp']

        self.FILE_NAME = ''
        self.FILE_EXTENSION = ''

        self.files_list = []

    def extractData(self):
        # Check if files are accepted      

        for file in os.listdir(self.WATCH_PATH):
            
            format_accepted = False
            
            for file_format in self.accept_pattern:
            
                if file_format in file: # Format is an accpeted pattern
            
                    format_accepted = True
            
                    self.files_list.append(file)
                    self.FILE_NAME, self.FILE_EXTENSION = file.split('.')

                    # 3 C
                    NEW_FILE_NAME = self.FILE_NAME + '_' + self.FILE_EXTENSION # Subtittles

                    source = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\Ejemplos Softni Files' + '\\' + self.FILE_NAME + '.' + self.FILE_EXTENSION
                    destination = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\RenamedFiles' + '\\' + NEW_FILE_NAME + '.' + self.FILE_EXTENSION

                    os.rename(source, destination) # Moves all the files
                    print('[!] File renamed and moved!')   
                    
                    # 3 D
                    # self.FILE_NAME = self.FILE_NAME.replace('06HD', '73HD')

                    # 3 E
                    # self.FILE_NAME = self.FILE_NAME.replace('73HD', '06HD')
                                # Checks language:
                    
                    for spanish_extension in self.SPANISH_EXTENSIONS:
                        if self.FILE_EXTENSION == spanish_extension:
                            self.isSpanish()
                        
                    for portuguese_extension in self.PORTUGUESE_EXTENSIONS:
                        if self.FILE_EXTENSION == portuguese_extension:
                            self.isPortuguese()
                    
                    for english_extension in self.ENGLISH_EXTENSIONS:
                        if self.FILE_EXTENSION == english_extension:
                            self.isEnglish()
                        
                if file_format == self.accept_pattern[-1] and not format_accepted:
                    print('[!] File ' + file + ' was no accepted.')
        
        print('[X] Done!')

        # 8

        if self.FILE_NAME == "H*" or self.FILE_NAME == "N*":
            pass # Copy

    def isSpanish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            print("[X] Spanish")
            #pass # Mufi Command

    def isPortuguese(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # Mufi Command

    def isEnglish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # Mufi Command
        

if __name__ == "__main__":
    rename = Rename()
    rename.extractData()