class ZipperTaskWindow(ctk.CTkToplevel):
    """mainly progress bar stuff"""
    def __init__(self, parent):
        super().__init__(parent)

        self.task_running = False
        self.task_path = r'C:\Users\mmoran\Projects\Git-Repos\MechTabby\python\App-Framework\resources\task.bat'
        self.proc = None
        self.percent = 0

        self.title("Task Window")
        self.center_window(550,260)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        self.resizable(False,False)

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
        self.percent_label = ctk.CTkLabel(self,text=f"Progress: 0%")
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
