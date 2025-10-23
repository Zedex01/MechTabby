import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import time

class Application(ctk.CTk): #Application IS a tkinter is an instance
    def __init__(self): #Create a constructor based on super
        super().__init__()

        self.title("Simple App")
        self.center_window(500,300)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        frame1 = InputForm(self)
        frame1.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)
        frame2 = InputForm(self)
        frame2.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)

        self.toplevel_window = None


    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow(self) #Create window if None or destoryed
            self.toplevel_window.grab_set() #Prevent interaction with parent
            self.toplevel_window.focus_set() #Set focus on self
            self.toplevel_window.transient(self) #Keep toplevel over main
        else:
            self.toplevel_window.focus() #Focus already existing window

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


class InputForm(ctk.CTkFrame):
    def __init__(self, parent): #Needs to know it who it belongs to "parent"
        super().__init__(parent) #Create constructor matching super
        self.parent = parent
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        #Takes self as the frame entry
        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=0, column = 0, sticky="ew")

        self.entry.bind("<Return>", self.add_to_list) #Calls function on key bress when in entry?

        self.entry_btn = ctk.CTkButton(self, text="Add", command=self.parent.open_login)
        self.entry_btn.grid(row=0,column=1)

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan= 2, sticky="nsew")


    def add_to_list(self, _event=None):
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def clear_list(self):
        self.text_list.delete(0, tk.END)

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


class LoginPopup(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("User Login")
        self.center_window(300,150)

        self.columnconfigure(0,weight=1)

        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0,column=0,padx=10,pady=10,sticky="nesw")

        #frame Grid Configs
        self.frame.columnconfigure(0,weight=0)
        self.frame.columnconfigure(1,weight=1)
        self.frame.columnconfigure(2,weight=1)

        self.frame.rowconfigure(0,weight=1)
        self.frame.rowconfigure(1,weight=1)
        self.frame.rowconfigure(2,weight=1)
        self.frame.rowconfigure(3,weight=1)

        #User Login Row
        self.user_label = ctk.CTkLabel(self.frame,text="Username:",anchor="e")
        self.user_label.grid(row=0,column=0, sticky="ew", padx=(10,5), pady=(10,5))
        self.user_entry = ctk.CTkEntry(self.frame)
        self.user_entry.grid(row=0, column=1, columnspan=2,sticky="ew", padx=(5,10), pady=(10,5))

        #Password Login Row
        self.password_label = ctk.CTkLabel(self.frame,text="Password:",anchor="e")
        self.password_label.grid(row=1,column=0, sticky="ew", padx=(10,5), pady=(5,10))
        self.password_entry = ctk.CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, columnspan=2,sticky="ew", padx=(5,10), pady=(5,10))

        #Info row
        self.info_label = ctk.CTkLabel(self.frame,text="This is a sample notice", bg_color="#f542a7",fg_color="#3818a1")
        self.info_label.grid(row=2, column=0, columnspan=3,sticky="we",padx=(10),pady=(5,5))

        #Buttons
        self.button_width = 70
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.grid(row=3,column=0,columnspan=3,sticky="we")
        
        self.button_frame.columnconfigure(0,weight=1) #This column will expand but the others do not
        self.button_frame.columnconfigure(1,weight=0)
        self.button_frame.columnconfigure(2,weight=0)

        self.cancel_button = ctk.CTkButton(self.button_frame,text="Cancel",width=self.button_width)
        self.cancel_button.grid(row=0,column=1,padx=(10,5), sticky="e")
        self.login_button = ctk.CTkButton(self.button_frame,text="Login",width=self.button_width)
        self.login_button.grid(row=0,column=2,padx=(5,10), sticky="e")


        #on enter try to login
        self.user_entry.bind("<Return>", command=self.attempt_login)
        self.password_entry.bind("<Return>", command=self.attempt_login)

    
    def attempt_login(self, _event=None):
        user = None
        password = None

        #Get text from entrywidget
        user = self.user_entry.get() 
        password = self.password_entry.get() 
        
        #Clear entrys
        #self.user_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)

        #place cursor pack in user field
        #self.user_entry.focus()






    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')

#Create Instance of tkinter
app = Application()

#Start said instance
app.mainloop()
