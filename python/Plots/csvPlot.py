from pathlib import Path
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# === Paths ===
if getattr(sys, 'frozen', False):
	root_dir = Path(sys._MEIPASS).parent
else:
	root_dir = Path(__file__).parent


Tk().withdraw()  # Hide the root window
file_path = askopenfilename()

if file_path:
    with open(file_path, "r") as f:
        print(f.read())