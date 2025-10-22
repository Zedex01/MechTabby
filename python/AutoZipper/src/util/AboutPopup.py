import customtkinter as ctk
'''
Responsible for contact, version# and attributions:
'''

class AboutPopup(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("About")
        self.center_window(400, 150)
        self.resizable(False, False)

        content = "Developer: Matt Moran\nVersion: 0.1\nBuild Date: 2025 10 21\nAttributions: Icons Provided by www.vecteezy.com"
        self.label = ctk.CTkLabel(self, text=content)
        self.label.pack(pady=10)

        #For closing window
        self.protocol("WM_DELETE_WINDOW", self.cancel)

# ================= Helpers ==============================
    

    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")


