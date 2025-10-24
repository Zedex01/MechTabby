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
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1,weight=1)

        frame1 = InputForm(self)
        frame1.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)
        frame2 = InputForm(self)
        frame2.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)

        frame3 = ctk.CTkFrame(self)
        frame3.grid(row=1,column = 0, columnspan=2, sticky ="nsew",padx=5,pady=5)

        self.login_btn = ctk.CTkButton(frame3, text="Login",command=self.open_login)
        self.login_btn.grid(row=0,column=0)
        self.login_btn = ctk.CTkButton(frame3, text="DoTask",command=self.open_task_window)
        self.login_btn.grid(row=0,column=1)

        self.toplevel_window = None
        self.task_window = None


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
        self.center_window(325,160)
        self.resizable(False,False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
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
        self.password_label.grid(row=1,column=0, sticky="ew", padx=(10,5), pady=(5,0))
        self.password_entry = ctk.CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, columnspan=2,sticky="ew", padx=(5,10), pady=(5,0))

        #Info row
        self.info_label = ctk.CTkLabel(self.frame,text=None, anchor="w",text_color="#e83427")
        self.info_label.grid(row=2, column=0, columnspan=3,sticky="we",padx=(10))

        #Buttons
        self.button_width = 70
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.grid(row=3,column=0,columnspan=3,sticky="we")
        
        self.button_frame.columnconfigure(0,weight=1) #This column will expand but the others do not
        self.button_frame.columnconfigure(1,weight=0)
        self.button_frame.columnconfigure(2,weight=0)

        self.cancel_button = ctk.CTkButton(self.button_frame,text="Cancel",width=self.button_width,command=self.cancel)
        self.cancel_button.grid(row=0,column=1,padx=(10,5),pady=5, sticky="e")
        self.login_button = ctk.CTkButton(self.button_frame,text="Login",width=self.button_width, command=self.attempt_login)
        self.login_button.grid(row=0,column=2,padx=(5,10), pady=5 ,sticky="e")

        #binds
        self.user_entry.bind("<Return>", command=self.attempt_login)
        self.password_entry.bind("<Return>", command=self.attempt_login)

    def cancel(self, _event=None):
        self.destroy()
    
    def attempt_login(self, _event=None):
        self.user = None
        password = None

        #Get text from entrywidget
        self.user = str(self.user_entry.get()) 
        password = (self.password_entry.get()) 
        def_color = self.password_label.cget("text_color")

        if self.user == "admin" and password == "mm":
            self.do_task()
            self.destroy()

        else:
            #Highlight content in entry
            self.password_entry.select_range(0,tk.END)
    
            #place cursor pack in password field
            self.password_entry.focus()
            #self.update_notice("*Incorrect login information")
            
            pause = 250
            notice = "Invalid Credentials"
            #Flash in red
            for i in range(0,4,2):
                self.after(pause*(i+1), lambda: self.update_notice(notice, "#e83427"))
                self.after(pause*(i+2), lambda: self.update_notice(notice, def_color))

    def update_notice(self, text, color):
        self.info_label.configure(text=text, text_color=color)
    
    def do_task(self):
        print(f"Welcome {self.user}!")

    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")

class TaskWindow(ctk.CTkToplevel):
    """mainly progress bar stuff"""
    def __init__(self, parent):
        super().__init__(parent)

        self.task_running = False
        self.task_path = r'C:\Users\mmoran\Projects\Git-Repos\MechTabby\python\App-Framework\resources\task.bat'
        self.proc = None
        self.percent = 0

        self.title("Task Window")
        self.center_window(400,300)

        self.percent_label = ctk.CTkLabel(self,text=f"Progress: 0%")
        self.percent_label.pack(padx=10, pady=10)

        self.content_box = ctk.CTkFrame(self, height=40, width=100)
        self.content_box.pack(padx=10,pady=10)

        #Progress bar:
        self.progress_bar = ctk.CTkProgressBar(self, orientation="horizontal", height=20, corner_radius=7)

        self.progress_bar.pack(padx=10,pady=10)
        self.progress_bar.set(0)

        self.cancel_btn = ctk.CTkButton(self, text="Cancel", command=self.cancel_task)
        self.cancel_btn.pack(padx=10,pady=10)

        #Start Task on window launch if no other task is running
        if self.task_running is False:
            #Setup thread with callback function
            thread = threading.Thread(target=self.task,args=(self.progress_callback,), daemon=True).start()

    def progress_callback(self, percent):
        #recieve the parameter from percent
        #Set global percent value recieve from callback
        self.percent = percent
        self.after(100, lambda:self.update())

    def update(self):
        #update all the important stuff on the gui
        self.progress_bar.set(self.percent)
        self.percent_label.configure(text=f"Progress {int(self.percent*100)}%")
        
        if self.percent == 1:
            self.task_running = False
            self.cancel_btn.configure(text="Finish", command=self.destroy)

    def task(self, callback):
        self.task_running = True
        #Create Process and have it redirect output to stdout
        self.proc = subprocess.Popen(
            self.task_path, 
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
            )

        #Read the stdout from the process
        for line in self.proc.stdout:
            line = line.strip()
            #Get result
            match = re.search(r'(\d+)%', line)
            if match:
                percent = (int(match.group(1))/100)
                #We call progress_callback giving it percent as an argument
                callback(percent)
                
    def cancel_task(self):
        #Check if task exists
        if self.proc is not None:
            try:
                self.proc.kill()
                self.task_running = False
                print("Task Killed")
                self.destroy()

            except Exception as e:
                print(f"Unable to kill: {e}")


    def update_task_window(self, percent):

        self.progress_bar.set(percent)
        


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
