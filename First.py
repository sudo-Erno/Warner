import sys
import os

class Rename():

    def __init__(self, path = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\Ejemplos Softni Files',
                destination = r'C:\Users\Erno\Documents\Programas Atom\Python\Warner\RenamedFiles'):
        # self.WATCH_PATH = "./Warner/Ejemplos Softni Files"
        self.path = path
        self.accepted_patterns = [".spa", ".por", ".eng", ".pop", ".spp", ".enp", ".SPA", ".ENG", ".POR"]

        self.FILE_PATH = ""
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
                    NEW_FILE_NAME = self.FILE_NAME + '_' + self.FILE_EXTENSION

                    # Testing directories
                    self.path = self.path + '\\' + self.FILE_NAME + '.' + self.FILE_EXTENSION
                    self.destination = self.destination + '\\' + NEW_FILE_NAME + '.' + self.FILE_EXTENSION

                    os.rename(self.path, self.destination) # Moves all files
        
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
                if self.FILE_NAME != "*SpaF*" and self.FILE_NAME != "*EngF*" and self.FILE_NAME != "*PorF*" and self.FILE_NAME != "H*" and self.FILE_NAME != "N*":
                    self.isFullSubtitle()
                
                # 9
                if self.FILE_NAME == "H*" or self.FILE_NAME == "N*":
                    self.isPromo()

                # 10
                # 11
                # 12

        print('[X] Done!')

    def isSpanish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_2997_spa: SMPTE-2997s:VTT-2997s: SRT-2997s: LegacyVoD_2997_spa:”

        
        elif self.FILE_NAME == 'H*' or self.FILE_NAME == 'N*' and self.FILE_NAME != '*P':
            pass # “C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_IN00_spa: SMPTE-2052-IN00s: VTT-IN00s: SRT-IN00-s:”

    def isPortuguese(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_2997_por: SMPTE-2997p:VTT-2997p: SRT-2997p: LegacyVoD_2997_por:
        
        elif self.FILE_NAME == 'H*' or self.FILE_NAME == 'N*' and self.FILE_NAME != '*P':
            pass # C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_IN00_por: SMPTE-2052-IN00p: VTT-IN00p: SRT-IN00-p:

    def isEnglish(self):
        if self.FILE_NAME != '*P' and self.FILE_NAME != '*73HD*' and self.FILE_NAME != 'H*' and self.FILE_NAME != 'N*':
            pass # C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_2997_eng: SMPTE-2997e:VTT-2997e: SRT-2997e: LegacyVoD_2997_eng:

        elif self.FILE_NAME == 'H*' or self.FILE_NAME == 'N*' and self.FILE_NAME != '*P':
            pass # C:\ProgramData\Vod_Mufi_V2_0-18\SoftNI-SFT.exe "HBO Subtitle File" owrite: HBOVoD_IN00_eng: SMPTE-2052-IN00e: VTT-IN00e: SRT-IN00-e:

    def isFullSubtitle(self):
        pass
    
    def isPromo(self):
        pass


rename = Rename()
rename.extractData()