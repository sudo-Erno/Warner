import os

class Rename():
    def __init__(self, path = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\Ejemplos Softni Files',
                destination = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\RenamedFiles'):
        
        self.path = path
        self.destination = destination
        self.accepted_patterns = [".spa", ".por", ".eng", ".pop", ".spp", ".enp", ".SPA", ".ENG", ".POR"]

        self.FILE_NAME = ''
        self.FILE_EXTENSION = ''
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
                    NEW_FILE_NAME = self.FILE_NAME + '_' + self.FILE_EXTENSION

                    # Testing directories for renaming the files
                    source = self.path + '\\' + self.FILE_NAME + '.' + self.FILE_EXTENSION
                    final_destination = self.destination + '\\' + NEW_FILE_NAME + '.' + self.FILE_EXTENSION

                    os.rename(source, final_destination)

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
                    if self.FILE_NAME != '*SpaF*' and self.FILE_NAME != '*EngF*' and self.FILE_NAME != '*PorF*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
                        self.isNotPartialSubtitle()
                    
                    # 12
                    # 13
                    # 14
                if file_format == self.accepted_patterns[-1] and not format_accepted:
                    print('[!] File ' + file + ' was no accepted.')

    def isSpanish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_2997_spa: SMPTE-2997s:VTT-2997s: SRT-2997s: HBOMAX_spa_2997: LegacyVoD_2997_spa:”
        
        new_file_name = self.FILE_NAME.replace('77HD-SpaF', '06HD_spp')

        # Commands...

    def isPortuguese(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_2997_por: SMPTE-2997p:VTT-2997p: SRT-2997p: HBOMAX_por_2997: LegacyVoD_2997_por:

        new_file_name = self.FILE_NAME.replace('78HD-PorF', '06HD_pop')

        # Commmands...

    def isEnglish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_2997_eng: SMPTE-2997e:VTT-2997e: SRT-2997e: HBOMAX_eng_2997: LegacyVoD_2997_eng:
        
        new_file_name = self.FILE_NAME.replace('76HD-EngF', '06HD_enp')

        # Commands...

    def isNotPartialSubtitle(self):
        pass # Commands....

if __name__ == "__main__":
    rename = Rename()
    rename.extractData()
