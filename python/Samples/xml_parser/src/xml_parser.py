import xml.etree.ElementTree as et
from pathlib import Path

class XMLParser():
    def __init__(self, file = None):
        if file:
            self.file = Path(file)

    def set_file(self, file):
        self.file = Path(file)



if __name__ == "__main__":
    #Get base path depending if script or exe
    if getattr(sys, 'frozen', False):
        base_path = os.path.join(sys._MEIPASS, "data", "config")
    else:
       root = Path(__file__)
       print("Path: ", root)
    
    xml = XMLParser()
    