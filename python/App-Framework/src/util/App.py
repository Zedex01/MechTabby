import customtkinter as ctk
from util.Popup import *


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('green')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sample App")
        self.center_window(400, 500)
        self.resizable(False, False)
        
        #Create frame to hold widgets:
        self.frame = ctk.CTkFrame(self,corner_radius=8)
        self.frame.pack(side="top", padx=20,pady=20,fill="both", expand=True)
        self.frame.pack_propagate(False)

        self.textbox = ctk.CTkTextbox(self.frame, corner_radius=8, font=("Consolas", 14))
        self.textbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.button = ctk.CTkButton(self.frame, text="Popup", command=self.open_popup)
        self.button.pack(side="right", pady=10, padx= 10)

    def open_popup(self):
        popup = Popup(self)
        popup.transient(self) #Bring to front?
        popup.grab_set() #Locks to this window untill closed
        popup.focus() #Sets mous + Keyboard to this windw?

  
    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")





