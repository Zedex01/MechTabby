import customtkinter as ctk

class ProgressPopup(ctk.CTkToplevel):
    def __init__(self, master, total_files):
        super().__init__(master)
        self.title("File Transfer")
        #self.geometry("400x150")
        self.center_window(400, 150)
        self.resizable(False, False)

        self.total_files = total_files
        self.current = 0
        self.cancelled = False

        self.label = ctk.CTkLabel(self, text=f"Moving 0 / {total_files} files...")
        self.label.pack(pady=10)

        self.progress=ctk.CTkProgressBar(self)
        self.progress.pack(padx=20, fill="x", pady=10)
        self.progress.set(0)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.cancel)
        self.cancel_button.pack(pady=5)

        self.protocol("WM_DELETE_WINDOW", self.cancel)

    def update_progress(self, moved):
        if not self.winfo_exists():
            return
        self.current = moved
        self.progress.set(moved/self.total_files)
        self.label.configure(text=f"Moving {moved} / {self.total_files} Parts...")
        self.update_idletasks()
    
    def cancel (self):
        self.cancelled = True
        self.destroy()

    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")