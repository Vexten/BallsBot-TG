import os
import json

class LocaleGetter():
    """
    Support class for getting a dictionary of localized message strings
    """
    def __init__(self, locale_folder : str):
        self.__dict = dict()
        self.__folder = locale_folder
    
    def __load_locale_files(self) -> None:
        for locale in os.listdir(self.__folder):
            f = os.path.join(self.__folder, locale)
            if os.path.isfile(f):
                f = open(f,encoding="utf_8_sig")
                self.__dict[locale.replace('.json','')] = json.load(f)
                f.close()
    
    def get_message_strings(self) -> dict:
        self.__load_locale_files()
        return self.__dict