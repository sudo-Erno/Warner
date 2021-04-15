import os

class Rename():

    def __init__(self, path = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\Ejemplos Softni Files',
                destination = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\RenamedFiles'):

        self.path = path
        self.destination = destination

        self.accepted_patterns = [".spa", ".por", ".eng", ".pop", ".spp", ".enp", ".SPA", ".ENG", ".POR"]

        self.FILE_EXTENSION = ""
        self.FILE_NAME = ""
        self.file_list = []
        self.partial_subtitle = ""
        self.SUBTITLES = ""

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

                    # 9
                    if 'SpaF' in self.FILE_NAME:
                        self.containsSpaF()
                    # 10
                    elif 'PorF' in self.FILE_NAME:
                        self.containsPorF()
                    
                    # 11
                    elif 'EngF' in self.FILE_NAME:
                        self.containsEngF()
                    # 8
                    else:
                        self.notLanguage()

                    # 12

                if file_format == self.accepted_patterns[-1] and not format_accepted:
                        print('[!] File ' + file + ' was no accepted.')


        print('[X] Done!')

    def isSpanish(self):

        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*':
            pass # “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2997s:”

        elif self.FILE_NAME == '*P' or self.FILE_NAME == '*73HD*':
            pass # Mufi Command C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2398s:

    def isPortuguese(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*':
            pass # Mufi Command  “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2997p:”

        elif self.FILE_NAME == '*P' or self.FILE_NAME == '*73HD*':
            pass # Mufi Command C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2398p:

    def isEnglish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*':
            pass # Mufi Command “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2997e:”

        elif self.FILE_NAME == '*P' or self.FILE_NAME == '*73HD*':
            pass #Mufi Command C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: SDVI_2398e:

    def notLanguage(self, path = '\\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\Filename_xxx.xml'):
        file_name = path.split('\\')[-1]
        mufi_name, file_extension = file_name.split('.')

        # Commands...
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_xxx.xml
        # to
        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"Mufi_name_xxx".ttml
        # Move and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_xxx.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"Mufi_name_xxx".ttml

    def containsSpaF(self):
        file_name = self.FILE_NAME
        file_name = file_name.replace('77HD-SpaF', '06HD_spp')
        # Commands...
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_spa.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\RSU\Watchfolder\SUBTITLES\TTML\"New File Name".ttml
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_spa.xml
        # to
        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"New File Name".ttml
        # Move and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_spa.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"New File Name".ttml
     
    def containsPorF(self):
        file_name = self.FILE_NAME
        file_name = file_name.replace('78HD-PorF', '06HD_pop')

        # Commands...
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_por.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\RSU\Watchfolder\SUBTITLES\TTML\"New File Name".ttml
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_por.xml
        # to
        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"New File Name".ttml
        # Move and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_por.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"New File Name".ttml
        
    def containsEngF(self):
        file_name = self.FILE_NAME
        file_name = file_name.replace('76HD-EngF', '06HD_enp')

        # Commands...
        # opy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_eng.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\RSU\Watchfolder\SUBTITLES\TTML\"New File Name".ttml
        # Copy and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_eng.xml
        # to
        # S3://hbola-sdvi-prod-input.s3.amazonaws.com/"New File Name".ttml
        # Move and Rename xml (owrite)
        # \\svrhsuvnp38\ProgramData\Vod_Mufi_V2_0-18\Files\SDVI\”Filename”_eng.xml
        # to
        # \\mdsnas-data.hbo-lag.com\DaletVOD\DPSHARE\LSU\Subtitles\SDVI_TTML\"New File Name".ttml

if __name__ == '__main__':
    rename = Rename()
    rename.extractData()