import sys
from shutil import copyfile

# 1
watch_path = "//mdsnas-data.hbo-lag.com/Watchfolders/Subtitles/IN_SDVI/"
accept_pattern = [".spa", ".por", ".eng", ".pop", ".spp", ".enp"]

# 2
file_path = ""
file_name = ""
file_name_no_extension = ""
file_extension = ""

if __name__ == "__main__":
    
    # 3
    if "--file" in sys.argv:

        file_name = sys.argv[len(sys.argv) - 1].split("\\")[-1]
        file_path = watch_path + file_name
        # 3A
        file_name_no_extension, file_extension = file_name.split(".")
        
        # 3B
        file_path = "src:" + file_path

        # 3C - 3D - 3E
        partial_subtitle = file_name_no_extension
        if "-EngP" in partial_subtitle:
            partial_subtitle = partial_subtitle.replace("-EngP", "_enp")
        
        elif "-SpaF" in partial_subtitle:
            partial_subtitle = partial_subtitle.replace("-SpaF", "_spp")
        
        elif "-PorF" in partial_subtitle:
            partial_subtitle = partial_subtitle.replace("-Porf", "_pop")

        # F
        subtitles = file_name_no_extension + "_" + file_extension + ".*"

        languages_list = [".spa", ".por", ".eng", ".SPA", ".POR", ".ENG", ".spp", ".enp", ".pop"]

        for language in languages_list:
            if language in file_name:
                # 5
                if language == ".spa" or language == ".SPA" or language == ".spp":
                    if file_name != "*P" and file_name != "*73HD":
                        pass # Mufi Command
                    if file_name == "*P" or file_name == "*73HD":
                        pass # Mufi Command

                # 6
                if language == ".por" or language == ".POR" or language == ".pop":
                    if file_name != "*P" and file_name != "*73HD":
                        pass # Mufi Command
                    if file_name == "*P" or file_name == "*73HD":
                        pass # Mufi Command
                
                # 7
                if language == ".eng" or language == ".ENG" or language == ".enp":
                    if file_name != "*P" and file_name != "*73HD":
                        pass # Mufi Command
                    if file_name == "*P" or file_name == "*73HD":
                        pass # Mufi Command
        
        # 8
        if file_name != "*SpaF*" and file_name != "*EngF*" and file_name != "*PorF*":
            # A
            # fp - File Path
            # fn - File Name
            # fe - File Extension
            fp = "//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}.xml".format(file_name)
            fn = file_name_no_extension + ".xml"
            fe = "xml"
            # B
            mufi_name = file_name
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}.xml".format(file_name), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}.ttml".format(mufi_name))
            except:
                print("[!] Could not copy the file to the desire path.")
            
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(mufi_name))
            except:
                print("[!] Could not move the file to the desire path.")

        # 9 En el PDF dice 'SpaF*', pero luego dice 'SpaF'...asumo por la segunda opcion        
        # Si es SpaF
        if "SpaF" in file_name:
            # A
            # nfn - New File Name
            nfn = file_name_no_extension
            if "77HD-SpaF" in file_name_no_extension:
                nfn = nfn.replace("77HD-SpaF", "06HD_spp")

            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_spa.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/RSU/Watchfolder/SUBTITLES/TTML/{}.ttml".format(nfn))
            except:
                print("[!] Could not copy the file to the desire path.")
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_spa.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}.ttml".format(nfn))
            except:
                print("[!] Could not copy the file to the desire path.")
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_spa.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(nfn))
            except:
                print("[!] Could not move the file to the desire path.")
            
        # Si es PorF
        if "PorF" in file_name:
            nfn = file_name_no_extension
            if "78HD-PorF" in nfn:
                nfn = nfn.replace("78HD-PorF", "06HD_pop")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/RSU/Watchfolder/SUBTITLES/TTML/{}.ttml".format(nfn))
            except:
                print("[!] Could not copy the file to the desire path.")
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_por.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}.ttml".format(nfn))
            except:
                print("[!] Could not copy the file to the desire path.")
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_por.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(nfn))
            except:
                print("[!] Could not move the file to the desire path.")

        # Si es EngF
        if "EngF" in file_name:
            nfn = file_name_no_extension
            if "76HD-EngF" in nfn:
                nfn = nfn.replace("76HD-EngF", "06HD_enp")

            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_eng.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/RSU/Watchfolder/SUBTITLES/TTML/{}.ttml".format(nfn))
            except:
                print("[!] Could not copy the file to the desire path.")
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_eng.xml".format(file_name_no_extension), "S3://hbola-sdvi-prod-input.s3.amazonaws.com/{}.ttml".format(nfn))
            except:
                print("[!] Could not copy the file to the desire path.")
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/SDVI/{}_eng.xml".format(file_name_no_extension), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/SDVI_TTML/{}.ttml".format(nfn))
            except:
                print("[!] Could not move the file to the desire path.")

        # 12
        try:
            shutil.move(file_path, "//mdsnas-data.hbo-lag.com/Watchfolders/Subtitles/IN_SDVI/Processed/{}".format(file_name))



        # print("[*] File Path: {}".format(file_path))
        
        
