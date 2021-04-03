import sys
from shutil import copyfile

# 1
watch_path = "//mdsnas-data.hbo-lag.com/Watchfolders/Subtitles/IN_SDVI_FrameConvert/"
accept_pattern = [".spa", ".por", ".eng", ".pop", ".spp", ".enp"]

# 2
file_path = ""
file_name = ""
file_name_no_extension = ""
file_extension = ""
partial_subtitle = ""
subtitles = ""

if __name__ == "__main__":
    
    # 3
    if "--file" in sys.argv:

        file_name = sys.argv[len(sys.argv) - 1].split("\\")[-1]
        file_path = watch_path + file_name
        # A
        file_name_no_extension, file_extension = file_name.split(".")
        
        # B
        file_path = "src:" + file_path

        # C
        if "-EngP" in file_name:
            partial_subtitle = file_name.replace("-EngP", "_enp")

        # D
        elif "-SpaF" in file_name:
            partial_subtitle = file_name.replace("-SpaF", "_spp")
        
        # E
        elif "-PorF" in file_name:
            partial_subtitle = file_name.replace("-PorF", "_pop")

        # F
        subtitles = file_name_no_extension + "_" + file_extension + ".*"
        
        # 4
        spanish_list = [".spa", ".SPA", ".spp"]
        portuguese_list = [".por", ".POR", ".pop"]
        english_list = [".eng", ".ENG", ".enp"]

        # 5
        for spa_lan in spanish_list:
            
            if spa_lan in file_name:
                
                if file_name != "*P" and file_name != "*73HD*":
                    pass # Mufi Command
            
                elif file_name == "*73HD*":
                    pass # Mufi Command
        
        # 6
        for por_lan in portuguese_list:
            
            if por_lan in file_name:
                
                if file_name != "*P" and file_name != "*73HD*":
                    pass # Mufi Command
                
                elif file_name == "*73HD":
                    pass # Mufi Command

        # 7
        for eng_lan in english_list:

            if eng_lan in file_name:

                if file_name != "*P" and file_name != "*73HD*":
                    pass # Mufi Command

                elif file_name == "*P" or file_name == "*73HD*":
                    pass # Mufi Command
        
        # 8
        if "06HD" in file_name or file_name_no_extension == "*06":
            
            # A
            fp = "//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}.xml".format(file_name_no_extension)

            # B
            mufi_name = file_name_no_extension

            # C
            mufi_name = mufi_name.replace("06HD", "73HD")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}.ttml".format(mufi_name))
            except:
                print("[!] Could not copy the file to the desire path.")
            
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(mufi_name))
            except:
                print("[!] Could not move the file to the desire path.")
        
        # 9 Aca devuelta, pone 'SpaF*', pero despues usan 'SpaF'
        fn_ne = file_name_no_extension
        if "SpaF*" file_name:            
                           
            new_file_name = fn_ne.replace("77HD-SpaF", "73HD_spp")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}_spa.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}_spa.ttml".format(file_name_no_extension))
            except:
                print("[!] Could not copy the file to the desire path.")
            
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}_spa.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(new_file_name))
            except:
                print("[!] Could not move the file to the desire path.")

        # 10
        if "PorF" file_name:            
                
            new_file_name = fn_ne.replace("78HD-PorF", "73HD_pop")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}_por.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}_por.ttml".format(file_name_no_extension))
            except:
                print("[!] Could not copy the file to the desire path.")
            
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398CONV/{}_por.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(new_file_name))
            except:
                print("[!] Could not move the file to the desire path.")

        # 11
        if "EngF" file_name:
                
            new_file_name = fn_ne.replace("76HD-EngF", "73HD_enp")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2398_CONV/{}_eng.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}_eng.ttml".format(file_name_no_extension))
            except:
                print("[!] Could not copy the file to the desire path.")
            
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/ SDVI_2398_CONV/{}_eng.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(new_file_name))
            except:
                print("[!] Could not move the file to the desire path.")

        # 12
        if "73HD" in file_name:
            
            # A
            fp = "//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2997CONV/{}_xxx.xml".format(file_name)
            fn = file_name + "_xxx" + ".xml"
            
            # B
            mufi_name = file_name + "_xxx"

            # C
            mufi_name = mufi_name.replace("73HD", "06HD")

        try:
            copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2997CONV/{}_xxx.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}.ttml".format(mufi_name))
        except:
            print("[!] Could not copy the file to the desire path.")
        
        try:
            shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI_2997CONV/{}_xxx.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(mufi_name))
        except:
            print("[!] Could not move the file to the desire path.")

        # 12
        try:
            shutil.move(file_path, "//mdsnas-data.hbo-lag.com/Watchfolders/Subtitles/IN_SDVI_FrameConvert/Processed/{}".format(file_name))
        except:
            print("[!] Could not move the file to the desire path.")
    
    print("[*] File Path: ", file_path)
    print("[*] File Name: ", file_name)
    print("[*] File Name No Extension: ", file_name_no_extension)
    print("[*] Subtitles: ", subtitles)
    print("[*] Partial Subtitle: ", partial_subtitle)
