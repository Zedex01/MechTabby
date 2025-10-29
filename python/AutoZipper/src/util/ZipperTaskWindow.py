import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

import threading, subprocess, re, datetime

from collections import deque

class ZipperTaskWindow(ctk.CTkToplevel):
    """mainly progress bar stuff"""
    def __init__(self, parent, cmd):
        super().__init__(parent)

        self.cmd = cmd
        self.task_running = False
        self.proc = None
        
        self.list = list

        self.title("7-Zip")
        self.center_window(550,260)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        self.resizable(False,False)

        self.display_percent = 0
        self.display_files = 0
        self.display_folders = 0
        self.display_curr = ""
        self.display_output = ""
        self.percent_changed = False

        #Get task start Time
        self.start_time = datetime.datetime.now()
        self.last_time = None
        print(self.start_time)

        self.dif = []

        #que for tracking avg times
        self.que = deque(maxlen=10)
        self.avg = 0
        self.formatted_time = "00:00:00.00"

        #==== Content Box ====
        self.content_box = ctk.CTkFrame(self, height=40, width=100)
        self.content_box.grid(row=0,column=0,padx=10,pady=(10,2),sticky="we")

        self.part_count_label = ctk.CTkLabel(self.content_box, text="# Parts Found", anchor="w")
        self.part_count_label.grid(row=0,column=0,padx=10,pady=(5,2),sticky="we")
        self.compressing_label = ctk.CTkLabel(self.content_box,text="Compressing x/y files", anchor="w")
        self.compressing_label.grid(row=1,column=0,padx=10,pady=(2),sticky="we")
        self.output_label = ctk.CTkLabel(self.content_box, text="Creating Archive: D:\Point Cloud Archives\20251027-110843\Archive-20251027-110384.7z", anchor="w")
        self.output_label.grid(row=2,column=0,padx=10,pady=(2,5),sticky="we")
        
        #Percent Done 
        self.percent_label = ctk.CTkLabel(self,text=f"Compressing: 0%")
        self.percent_label.grid(row=1, column=0,padx=10, pady=2,sticky="we")

        #Progress bar:
        self.progress_bar = ctk.CTkProgressBar(self, orientation="horizontal", height=20, corner_radius=7)
        self.progress_bar.grid(row=2,column=0,padx=10,pady=5,sticky="we")
        self.progress_bar.set(0)

        #Estimated time remaining
        self.est_time_label = ctk.CTkLabel(self, text="est. time remaining: ###",anchor="w")
        self.est_time_label.grid(row=3,column=0,padx=10,pady=2,sticky="we")

        #Cancel Btn
        self.cancel_btn = ctk.CTkButton(self, text="Cancel", command=self.cancel_task)
        self.cancel_btn.grid(row=4,column=0,padx=10,pady=10)

        #Run Cancel task on close:
        self.protocol("WM_DELETE_WINDOW", self.cancel_task)

        #Start Task on window launch if no other task is running
        if self.task_running is False:
            #Setup thread with callback function
            thread = threading.Thread(target=self.task,args=(self.progress_callback,), daemon=True).start()

    def progress_callback(self, data):
        #recieve the parameter from percent
        #Set global percent value recieve from callback

            
        #Check if the percent has changed
        if self.display_percent != data["percent"]:
            self.display_percent = data["percent"]
            self.percent_changed = True 

        self.display_files = data["files"]
        self.display_folders = data["folders"]
        self.display_output = data["output_path"]
        self.display_curr = data["curr_file"]
        #print(f"{self.display_percent}, {self.display_files}, {self.display_folders}, {self.display_output}, {self.display_curr}")
        self.after(100, lambda:self.update())

    def update(self):
        #if the window does not exist, return
        if not self.winfo_exists():
            return

        #If the percentage has changed run time estimation stuff
        if self.percent_changed:

            #If first change, set last time to start time
            if self.last_time == None:
                self.last_time = self.start_time

            #Will keep the most recent 10 values
            self.que.append(datetime.datetime.now() - self.last_time)
            #Set the last time
            self.last_time = datetime.datetime.now()

            #Gets the ave time within the que of 10
            self.avg = sum((delta.total_seconds() for delta in self.que)) / len(self.que)
            
            #Calculate and format remaining time
            self.remaining_time = (self.avg)*(100-int(self.display_percent))
            #self.formatted_time = str(datetime.timedelta(seconds=self.remaining_time))
            self.formatted_time = f"{int(self.remaining_time // 3600):02}:{int((self.remaining_time % 3600) // 60):02}:{self.remaining_time % 60:05.2f}"

        #update all the important stuff on the gui
        self.progress_bar.set(int(self.display_percent)/100)
        self.percent_label.configure(text=f"Compressing: {self.display_percent}%")
        self.part_count_label.configure(text=f"{self.display_folders} parts found")
        self.compressing_label.configure(text=f"Compressing {self.display_files} files")
        self.output_label.configure(text=f"Creating archive: {self.display_output}")
        self.est_time_label.configure(text=f"est. time left: {self.formatted_time}")
        
        #When complete, set cancel button to say done
        if self.display_percent == 100:
            self.task_running = False
            self.cancel_btn.configure(text="Finish", command=self.destroy)

    def task(self, callback):
        self.task_running = True
        self.percent = None

        #Create Process and have it redirect output to stdout
        self.proc = subprocess.Popen(
            self.cmd, 
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW
            )

        last = {
            "percent":None,
            "folders":None,
            "files":None,
            "curr_file":None,
            "output_path":None
        }

        #Read the stdout from the process
        for line in self.proc.stdout:
            line = line.strip()
            updated = False

            # Compile your patterns once
            pattern_percent = re.compile(r'(\d+)%')
            pattern_folders = re.compile(r'(\d+)\s+folders')
            pattern_files = re.compile(r'(\d+)\s+files')
            pattern_output = re.compile(r'Creating archive:\s+(.*)')
            pattern_curr = re.compile(r'\d+%.{1,7}(\d{7}\\.*)')

            # --- Check for output path ---
            match = pattern_output.search(line)
            if match:
                output_path = match.group(1)
                if output_path != last["output_path"]:
                    last["output_path"] = output_path
                    updated = True

            # --- Check folders ---
            match = pattern_folders.search(line)
            if match:
                folders = int(match.group(1))
                if folders != last["folders"]:
                    last["folders"] = folders
                    updated = True

            # --- Check files ---
            match = pattern_files.search(line)
            if match:
                files = int(match.group(1))
                if files != last["files"]:
                    last["files"] = files
                    updated = True

            # --- Check percent ---
            match = pattern_percent.search(line)
            if match:
                self.percent = int(match.group(1))
                if self.percent != last["percent"]:
                    last["percent"] = self.percent
                    updated = True

            match = pattern_curr.search(line)
            if match:
                curr_file = match.group(1)
                if curr_file != last["curr_file"]:
                    last["curr_file"] = curr_file
                    updated = True
           
            #Send the results back to parent
            if updated is True:
                if self.percent is not None:
                    callback(last)
           
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

    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")
