import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import os
import win32com.client
from util.Selector import Selector
from util.ProgressPopup import ProgressPopup
import threading
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Point Cloud Filter System")
        #self.geometry("400x500")
        self.center_window(400, 500)
        self.resizable(False, False)
        
        #Create frame to hold widgets:
        self.frame = ctk.CTkFrame(self,corner_radius=8)
        self.frame.pack(side="top", padx=20,pady=20,fill="both", expand=True)
        self.frame.pack_propagate(False)

        #Text widget:
        self.textbox = ctk.CTkTextbox(self.frame, corner_radius=8, font=("Consolas", 14))
        self.textbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.button = ctk.CTkButton(self.frame, text="Sort", command=self.filter)#Don't include the () for the button, otherwise it will be called on creation
        self.button.pack(side="right", pady=10, padx= 10)

    
    
    def filter(self):
        print("Filtering!")

        content_list = []
        content = self.textbox.get("1.0", tk.END)
        content = content.split("\n")
        content = [line for line in content if line.strip() != ""]

        for line in content:
            print(line)
            content_list.append(line.strip())

        if len(content) == 0:
            return

        sel = Selector()
        sel.add_to_list(content_list)
        file_count = sel.get_total_files()
        print(f"Files To Move: {file_count}")

        if file_count > 0:
            self.popup = ProgressPopup(self, file_count)
            self.popup.transient(self)
            self.popup.update()

            thread = threading.Thread(target=self.move_files,args=(sel,), daemon=True)
            thread.start()

            #Highlight Selector
            self.check_thread(thread, sel)

        else:
            sel.filter_dirs()

    def move_files(self, sel):
        sel.move_folders(self.popup)

    def check_thread(self, thread, sel):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread, sel))
        else:
            # Thread finished, now run your post-processing
            sel.filter_dirs()

    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")





