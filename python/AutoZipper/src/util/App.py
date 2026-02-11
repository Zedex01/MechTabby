import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import os
import win32com.client
from util.Selector import Selector
from util.ProgressPopup import ProgressPopup
from util.AboutPopup import AboutPopup
import threading

#For Message Box
import ctypes
MB_OK = 0x00000000
MB_ICONERROR = 0x00000010
MB_TASKMODAL = 0x00002000  # blocks interaction with the current app
#MB_OK | MB_ICONERROR | MB_TASKMODAL

from util.ZipperTaskWindow import ZipperTaskWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Point Cloud Zipper")
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

        self.button = ctk.CTkButton(self.frame, text="Grab & Zip", command=self.zip)
        self.button.pack(side="right", pady=10, padx=10)

        self.zip_window = None

    def zip(self):
        content_list = []
        content = self.textbox.get("1.0", tk.END)
        content = content.split("\n")
        content = [line for line in content if line.strip() != ""]

        for line in content:
            content_list.append(line.strip())

        #If There are no items in list, return
        if len(content) == 0:
            #Display a popup window to the user
            ctypes.windll.user32.MessageBoxW(0, "No serial numbers provided.", "AutoZipper", MB_OK | MB_ICONERROR | MB_TASKMODAL)
            return

        #Create Selector Object
        sel = Selector()
        sel.add_to_list(content_list)
        cmd = sel.zip_files()
        print("[*] sel.zip_files done")
        #Open Zipper Window, pass built cmd to window
        if cmd is not None:  
            if self.zip_window is None or not self.zip_window.winfo_exists():
                self.zip_window = ZipperTaskWindow(self, cmd)
                self.zip_window.focus_set()
                self.zip_window.transient(self)
            else:
                self.zip_window.focus() 
        else:
            print("[-] cmd is None")



    def filter(self):
        content_list = []
        content = self.textbox.get("1.0", tk.END)
        content = content.split("\n")
        content = [line for line in content if line.strip() != ""]

        for line in content:
            content_list.append(line.strip())

        if len(content) == 0:
            return

        sel = Selector()
        sel.add_to_list(content_list)
        file_count = sel.get_total_files()
        print(f"Files To Move: {file_count}")

        #Temp Bypass:
        file_count = 0
        if file_count > 0:
            self.popup = ProgressPopup(self, file_count)
            self.popup.transient(self)
            self.popup.update()

            thread = threading.Thread(target=self.move_files,args=(sel,), daemon=True)
            thread.start()

            #Highlight Selector
            self.check_thread(thread, sel)

        else:
            #Zip All Files
            sel.zip_files()

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





