"""
Matthew Moran 2025-11-05

File for helping keep track of resources and 
data for built applications using pyinstaller
 
"""
import sys, os

def get_base_path() -> str:
    #Path when running for .exe
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)

    #Path when running from source
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#get the path for the "data subfolder"
def get_data_path() -> str:
    base = get_base_path()
    return os.path.join(base, "data")

def get_database_path() -> str:
    data = get_data_path()
    return os.path.join(data, "database.db")

def get_config_path() -> str:
    data = get_data_path()
    return os.path.join(data, "config.ini")
