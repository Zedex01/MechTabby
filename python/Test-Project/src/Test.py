import sys
import tkinter as tk 
from tkinter import *


def main():
	build_window()
    
def build_window() -> None:
    print(f"Building Window...")
    
    root = tk.Tk()
    root.title("Test Application")
    
    #=== Menu ===
    menu = Menu(root)
    root.config(menu=menu) #Links menubar to main window
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    root.mainloop()
    
if __name__ == "__main__":
	main()