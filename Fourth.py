import os

class Rename():

    def __init__(self, path = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\Ejemplos Softni Files',
                destination = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\RenamedFiles'):
        
        self.path = path
        self.destination = destination
        self.accepted_patterns = [".spa", ".por", ".eng", ".pop", ".spp", ".enp", ".SPA", ".ENG", ".POR"]

        self.FILE_NAME = ""
        self.FILE_EXTENSION = ""
        self.file_list = []

        self.SPANISH_EXTENSIONS = ['.spa', '.SPA', '.spp']
        self.PORTUGUESE_EXTENSIONS = ['.por', '.POR', '.pop']
        self.ENGLISH_EXTENSIONS = ['.eng', '.ENG', '.enp']

    def extractData(self):
        
        for file in os.listdir(self.path):
            
            format_accepted = False

            for file_format in self.accepted_patterns:
                
                if file_format in file:

                    format_accepted = True

                    self.file_list.append(file)
                    self.FILE_NAME, self.FILE_EXTENSION = file.split('.')                    

                    # 3 C
                    partial_subtitle = self.FILE_NAME.replace('-SpaF', '_spp') # Spanish
                    partial_subtitle = self.FILE_NAME.replace('-EngP', '_enp') # English
                    partial_subtitle = self.FILE_NAME.replace('-PorF', '_pop') # Portuguese

                    # 3 F
                    self.SUBTITLES = partial_subtitle + '_' + self.FILE_EXTENSION

                    # Testing directories for renaming the files
                    source = self.path + '\\' + self.FILE_NAME + '.' + self.FILE_EXTENSION
                    final_destination = self.destination + '\\' + self.SUBTITLES + '.' + self.FILE_EXTENSION

                    os.rename(source, final_destination) # Moves all files

                    for spanish_extension in self.SPANISH_EXTENSIONS:
                        if self.FILE_EXTENSION == spanish_extension:
                            self.isSpanish()
                                
                    for portuguese_extension in self.PORTUGUESE_EXTENSIONS:
                        if self.FILE_EXTENSION == portuguese_extension:
                            self.isPortuguese()
                    
                    for english_extension in self.ENGLISH_EXTENSIONS:
                        if self.FILE_EXTENSION == english_extension:
                            self.isEnglish()

                    # 8
                    if '06HD' in self.FILE_NAME or '*06' in self.FILE_NAME:
                        self.language()
                    
                    # 9
                    if 'SpaF*' in self.FILE_NAME:
                        file_name = self.FILE_NAME.split('_')[0]
                        file_name = file_name.replace('77HD-SpaF', '73HD_spp')
                        
                        # Commands...
                        # Copy and Rename xml (owrite)
                        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398CONV\”Filename”_spa.xml
                        # to
                        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"File Name"_spa.ttml
                        # Move and Rename xml (owrite)
                        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398CONV\”Filename”_spa.xml
                        # to
                        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"New File Name".ttml

                    # 10
                    elif 'PorF' in self.FILE_NAME:
                        file_name = self.FILE_NAME.split('_')[0]
                        file_name = file_name.replace('78HD-PorF', '73HD_pop')
                        
                        # Commands...
                        # Copy and Rename xml (owrite)
                        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398CONV\”Filename”_por.xml
                        # to
                        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"File Name"_por.ttml
                        # Move and Rename xml (owrite)
                        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398_CONV\”Filename”_por.xml
                        # to
                        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"New File Name".ttml
                    elif 'EngF' in self.FILE_NAME:
                        file_name = self.FILE_NAME.splot('_')[0]
                        file_name = file_name.replace('76HD-EngF', '73HD_enp')

                        # Commands...
                        # Copy and Rename xml (owrite)
                        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398_CONV\”Filename”_eng.xml
                        # to
                        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"File Name"_eng.ttml
                        # Move and Rename xml (owrite)
                        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\ SDVI_2398_CONV\”Filename”_eng.xml
                        # to
                        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"New File Name".ttml

                    # 12
                    if '73HD' in self.FILE_NAME:
                        pass

                if file_format == self.accepted_patterns[-1] and not format_accepted:
                        print('[!] File ' + file + ' was no accepted.')

        print('[X] Done!')

    def isSpanish(self):
        if self.FILE_NAME != "*P" and self.FILE_NAME != "*73HD*":
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2398CONVs:”
        
        elif self.FILE_NAME == "*73HD*":
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2997CONVs:”

    def isPortuguese(self):
        if self.FILE_NAME != "*P" and self.FILE_NAME != "*73HD*":
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2398CONVp:”
                
        elif self.FILE_NAME == "*73HD":
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2997CONVp:”

    def isEnglish(self):
        if self.FILE_NAME != "*P" and self.FILE_NAME != "*73HD*":
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2398CONVe:”

        elif self.FILE_NAME == "*P" or self.FILE_NAME == "*73HD*":
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2997CONVe:”
        
    def language(self, path = '\\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398CONV\”Filename”_xxx.xml'):
        file_name = path.split('\\')[-1]
        mufi_name, file_extension = file_name.split('.')
        mufi_name = mufi_name.replace('06HD', '73HD')

        # Commands...
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398CONV\”Filename”_xxx.xml
        # to
        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"Rename to 06HD or 73HD".ttml
        # Move and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI_2398CONV\”Filename”_xxx.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"Rename to 06HD or 73HD".ttml
        pass


if __name__ == "__main__":
    
    rename = Rename()
    rename.extractData()
