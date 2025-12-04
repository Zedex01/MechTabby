import xml.etree.ElementTree as et
from pathlib import Path
import sys, os, csv
from tkinter import Tk, filedialog

class XMLParser():
    def __init__(self, file = None):
        if file:
            self.file = file

    def set_file(self, file):
        self.file = file



if __name__ == "__main__":
    #Get base path depending if script or exe
    if getattr(sys, 'frozen', False):
        base_path = os.path.join(sys._MEIPASS, "data", "config")
    else:
       root = Path(__file__).parent.parent    
    
    data = root / 'data'
    
    #Set output file location
    output_file = data / "JEC-Transforms.csv"

    #Create Window
    Tk().withdraw()
    #Prompt for file 
    input_file = filedialog.askopenfilename()
    #Convert to Path object
    file = Path(input_file)

    #Wipe and add heders to output file
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Point", "X", "Y", "Z", "W", "P", "R"])

    #Setup XML Tree
    tree = et.parse(file)
    tree_root = tree.getroot()

    #Model_List contains all the multipoint Alignments
    model_list = tree_root.find("Model_List")
    
    #Itterate through each Multi Point Alignment
    for model in model_list.findall("Model_Object"):
        tool = model.find("Tool") #MPA

        tool_id = tool.find("ID").text
        tool_name = tool.find("Name").text
        tool_type = tool.find("Type").text

        tf_matrix = tool.find("MultiPointsAlignment/mParams/FinalTFMatrix")

        axes = ["X", "Y", "Z", "W", "P", "R"]
        ctx = []

        ctx.append(tool_name)

        for axis in axes:
            ctx.append(tf_matrix.find(axis).text)
        try:
            """Format: Name, x, y, z, w, p, r"""
            output_string = ", ".join(ctx)
            print(output_string)

            with output_file.open("a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(ctx)
        except Exception as e:
            pass
   
        