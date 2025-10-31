import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import time, subprocess, threading, re

class Application(ctk.CTk): #Application IS a tkinter is an instance
    def __init__(self): #Create a constructor based on super
        super().__init__()

        self.title("Simple App")
        self.center_window(500,300)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        self.frame = CeaserForm(self)
        self.frame.grid(row=0,column=0,sticky="nsew")


    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow(self) #Create window if None or destoryed
            self.toplevel_window.grab_set() #Prevent interaction with parent
            self.toplevel_window.focus_set() #Set focus on self
            self.toplevel_window.transient(self) #Keep toplevel over main
        else:
            self.toplevel_window.focus() #Focus already existing window

    def open_task_window(self):
        if self.task_window is None or not self.task_window.winfo_exists():
            self.task_window = TaskWindow(self)
            self.task_window.focus_set()
            self.task_window.transient(self)
        else:
            self.task_window.focus()

    def open_login(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = LoginPopup(self) #Create window if None or destoryed
            self.toplevel_window.grab_set() #Prevent interaction with parent
            self.toplevel_window.focus_set() #Set focus on self
            self.toplevel_window.transient(self) #Keep toplevel over main
        else:
            self.toplevel_window.focus() #Focus already existing window
        
    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")    

    def error_popup(self):
        tk.messagebox.showerror(
            title="Error",
            message = "You can't do that..."
        )

    def input_dialog(self):
        dialog = ctk.CTkInputDialog(text="Number:", title="Input Box")
        text = dialog.get_input() #Waits for input
        print(text)

class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Custom Popup Window")
        self.center_window(300,140)
        self.label = ctk.CTkLabel(self, text="TopLevelWindow!")
        self.label.pack(padx=20,pady=20)

    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")


class CeaserForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)

        self.title_label=ctk.CTkLabel(self, text="Ceaser Cipher")
        self.title_label.grid(row=0, column=0, sticky="ew",padx=10,pady=10)

        self.input_box = ctk.CTkTextbox(self, height=35)
        self.input_box.grid(row=1, column=0,sticky="ew",padx=10,pady=2)
        
        self.decode_btn = ctk.CTkButton(self, text="decode", command=self.decode)
        self.decode_btn.grid(row=2, column=0, sticky="e", padx=10, pady=2)

        self.output_list = tk.Listbox(self, height=26)
        self.output_list.grid(row=3, column=0, sticky="ew",padx=10,pady=2)


    
    def decode(self):
        self.input_content = None
        self.output_list.delete(0,tk.END)
        self.input_content = self.input_box.get("1.0", "end-1c")
        
        out = []

        #A-Z = 65-90
        #a-z = 97-122
        #ord('A')  # → 65
        #chr(97)   # → 'a'
        length = len(self.input_content)
        print(f"length: {len(self.input_content)} | Content: {self.input_content}")
        for i in range(25):
            out = []
            for char in self.input_content:
                if char.isalpha():
                    ascii = ord(char)
                    ascii += 1
                    if ascii == 91:
                        ascii = 65
                    elif ascii == 123:
                        ascii = 97
                    char = chr(ascii)
                    out.append(char)
                else:
                    out.append(char)
            out = "".join(out)
            self.input_content = out
            self.output_list.insert(tk.END, out)



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')

#Create Instance of tkinter
app = Application()

#Start said instance
app.mainloop()
