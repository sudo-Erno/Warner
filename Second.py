import sys, os
from shutil import copyfile

# 1 - WatchFolder
watch_path = "//mdsnas-data.hbo-lag.com/Watchfolders/Subtitles/IN_2997_HBOMAX/"
accepted_patterns = [".spa", ".por", ".eng", ".pop", ".spp", ".enp"]

# 2 - Identify - Create Variables
file_path = ""
file_name = ""
file_name_no_extension = ""
file_extension = ""


if __name__ == "__main__":

    if "--file" in sys.argv:
        # 3 - Compute - CMD and Output Name
        file_path = sys.argv[len(sys.argv) - 1]

        file_name_no_extension = file_path.split(".")
        file_extension = file_name_no_extension[1]

        file_name_no_extension = file_name_no_extension[0].split("\\")[-1]
        file_name = file_name_no_extension + "." + file_extension

        # Test
        file_path = "src:" + watch_path + file_name_no_extension + "." + file_extension

        # C - Concatenate
        subtitles = file_name_no_extension + "_" + file_extension + ".*"

        # D & E - Replace Substring
        if "06HD" in file_name:
            file_name = file_name.replace("06HD", "73HD")
        elif "73HD" in file_name:
            file_name = file_name.replace("73HD", "06HD")

        # 4 - Decide - Search for Languages
        languages = ["spa", "por", "eng", "SPA", "POR", "ENG", "spp", "enp", "pop", "s", "p", "e"] # --> "Agregue las ultimas 3 segun lo que vi en el PDF."

        for language in languages:
            if language in file_name:
                
                # 5 - Decide - Search for "SPA" Languages
                if language == "spa" or language == "SPA" or language == "spp":
                    if file_name_no_extension != "*P" and file_name_no_extension != "*73HD" and file_name_no_extension != "H*" and file_name_no_extension != "N*":
                        # print("---Spanish---")
                        pass # Ni idea que hay que hacer
                
                # 6 - Decide - Search for "POR" Languages
                if language == "por" or language == "POR" or language == "pop":
                    if file_name_no_extension != "*P" and file_name_no_extension != "*73HD" and file_name_no_extension != "H*" and file_name_no_extension != "N*":
                        # print("---Portiguese---")
                        pass # Ni idea que hay que hacer
                
                # 7 - Decide - Search for "ENG" Languages
                if language == "eng" or language == "ENG" or language == "enp":
                    if file_name_no_extension != "*P" and file_name_no_extension != "*73HD" and file_name_no_extension != "H*" and file_name_no_extension != "N*":
                        # print("---English---")
                        pass # Ni idea que hay que hacer
                
        # 8 - Decide - Is not Partial Subtitle - Move/Copy converted Mufi files to final destinations
        if file_name_no_extension != "*SpaF*" and file_name_no_extension != "*EngF*" and file_name_no_extension != "*PorF*" and file_name_no_extension != "H*" and file_name_no_extension != "N*":
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "S3 “hbola-sdvi-prod-input” /{}.xml".format(file_name))
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/HBOMax_SMPTE/{}.xml".format(file_name))
            except:
                print("[!] Could not move the file to the desire path.")
                # sys.exit()
        
        # 9 - Decide Language - Spanish - Move/Copy converted Mufi files to final destinations
        new_file_name = file_name
        if "SpaF" in file_name:
                new_file_name = new_file_name.replace("77HD-SpaF", "06HD_spp")

            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/RSU/Watchfolder/SUBTITLES/TTML/{}.xml".format(new_file_name))
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "S3 “hbola-sdvi-prod-input” /{}.xml".format(new_file_name)) # Chequear que se agregue el '_spa'
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()

            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/HBOMax_SMPTE/{}.xml".format(new_file_name)) # Chequear que se agregue el '_spa'
            except:
                print("[!] Could not move the file to the desire path.")

        # 10 - Decide Language - Portuguese - Move/Copy converted Mufi files to final destinations
        if "PorF" in file_name:
            
            new_file_name = new_file_name.replace("78HD-PorF", "06HD_pop")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/RSU/Watchfolder/SUBTITLES/TTML/{}.xml".format(new_file_name))
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "S3 “hbola-sdvi-prod-input” \{}.xml".format(file_name))
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()

            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "\\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\HBOMax_SMPTE\{}.xml".format(new_file_name))
            except:
                print("[!] Could not move the file to the desire path.")
        
        # 11 - Decide Language - English - Move/Copy converted Mufi files to final destinations
        if "EngF" in file_name:
            new_file_name = new_file_name.replace("76HD-EngF", "06HD_enp")
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/RSU/Watchfolder/SUBTITLES/TTML/{}.xml".format(new_file_name))
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()
            
            try:
                copyfile("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "S3 “hbola-sdvi-prod-input” \{}.xml".format(file_name))
            except:
                print("[!] Could not copy the file to the desire path.")
                # sys.exit()
                
            try:
                shutil.move("//svrhsuvnp38/ProgramData/Vod_Mufi_V2_0-18/Files/HBOMAX_2997/{}.xml".format(file_name), "//mdsnas-data.hbo-lag.com/DaletVOD/DPSHARE/LSU/Subtitles/HBOMax_SMPTE/{}.xml".format(new_file_name))
            except:
                print("[!] Could not move the file to the desire path.")

        # 12 - Copy XML to S3 "HBOMAX_SMPTE"

        # 13 - Copy ORIGINAL to S3 Subtitle "SOFTNI_MASTERS"

        # 14 - Move ORIGINAL to "SDVI Vantage Workflow"
        print("\n")
        print("[*] File Path: {}".format(file_path))
        print("[*] File Name: {}".format(file_name_no_extension))
        print("[*] File Extension: {}".format(file_extension))
        print("[*] File Full Name: {}".format(file_name))
        print("[*] Subtitles: {}".format(subtitles))
        