""" Class for grabbing from config file"""
import configparser, os, sys

class Config:
    def __init__(self) -> None:

        #Get base path depending if script or exe
        if getattr(sys, 'frozen', False):
            base_path = os.path.join(sys._MEIPASS, "resources", "config")
        else:
            base_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "resources", "config")

        CONFIG_FILE = os.path.join(base_path, "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)
          
    def get_bool(self, section: str, key: str, fallback=False) -> bool:
        return self.config.getboolean(section, key, fallback=fallback)
    
    def get_str(self, section:str , key:str , fallback=None) -> str:
        return self.config.get(section, key, fallback=fallback)
        
    def get_int(self, section:str, key:str, fallback=-1) -> int:
        return self.config.getint(section, key, fallback=fallback)


