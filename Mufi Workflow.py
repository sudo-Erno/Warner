import sys
import os

present_working_dir = os.getcwd()

accepted_patterns = [".spa", ".por", ".eng", ".pop", ".spp", ".enp"]

file_path = ""
file_name = ""
file_extension = ""
subtitles_file = ""

if __name__ == "__main__":

    if "--help" in sys.argv:
        print("""[*] --path: Path of the folder (if the name of the folder has space(s), use '"' """)

    if "--path" in sys.argv:
        arg_index = sys.argv.index("--path")
        file_path = sys.argv[arg_index + 1]

        directory = ""

        for pattern in accepted_patterns:
            if pattern in file_path.lower():

                directory = file_path.split(".")[0]
                file_extension = file_path.split(".")[1]
                file_extension = file_extension.lower()

                file_name = directory.split("\\")[-1]

                source = directory.split(":")[0]
                source = "src:"
                subtitles_file = source + directory.split(":")[1]
                break

        print("Original Subtitles File: " + subtitles_file)
        print("Original File Name: " + file_name)
        print("File Extension: " + file_extension)
        print("\n")

        # C - Concatenate
        file_name = file_name + "_" + file_extension + ".*"

        # D & E - Replace Substring

        file_name_splited = file_name

        if "06HD" in file_name:
            file_name_splited.replace("06HD", "73HD")
            print("[*] File rename to 73HD")
            print("\n")

        elif "73HD" in file_name:
            file_name_splited.replace("73HD", "06HD")
            print("[*] File rename to 06HD")
            print("\n")
        
        print("Name after modification: " + file_name)



    
                
