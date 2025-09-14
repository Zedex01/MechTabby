""" Class for grabbing from config file"""
import configparser
import os

class Config:
    def __init__(self):
        CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "resources", "config", "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)
          
    def get_bool(self, section, key, fallback=False):
        return self.config.getboolean(section, key, fallback=fallback)
    
    def get_str(self, section, key, fallback = None):
        return self.config.get(section, key, fallback=fallback)
        
    def get_int(self, section, key, fallback=-1):
        return self.config.getint(section, key, fallback=fallback)


