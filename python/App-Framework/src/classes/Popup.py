import customtkinter as ctk

class Popup(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Popup Window")
        self.center_window(300,150)


        self.label = ctk.CTkLabel(self, text="This is a popup window!")
        self.label.pack(pady=20)

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(expand=True)

        #Check info frames
        self.check_frame = ctk.CTkFrame(self.main_frame, corner_radius=0)
        self.check_frame.pack(padx=10, pady=(10,0), expand = True)

        #self.use_volumes_label = ctk.CTkLabel(self.check_frame, text="Use Volumes: ")
        self.use_volumes_checkbox = ctk.CTkCheckBox(self.check_frame, text="Use Volumes")
        
        #self.use_volumes_label.pack(side="left",pady=5,padx=20)
        self.use_volumes_checkbox.pack(side="right",pady=5,padx=20)

        #Volume info Frames
        self.info_frame = ctk.CTkFrame(self.main_frame, corner_radius=0)
        self.info_frame.pack(padx=10, pady=(0,10),expand = True)

        self.volume_size_label = ctk.CTkLabel(self.info_frame, text="Volume Size:")
        self.volume_mb_entry = ctk.CTkEntry(self.info_frame, width=70, placeholder_text="1000")
        self.volume_mb_label = ctk.CTkLabel(self.info_frame, text="mb")

        self.volume_size_label.pack(side = "left", pady=5,padx=(20,5))
        self.volume_mb_entry.pack(side = "left", pady=5,)
        self.volume_mb_label.pack(side = "right", pady=5,padx=(5,20))



        self.button_close = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.button_close.pack(pady=10)


    def center_window(self, width: int, height: int):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # Apply geometry
        self.geometry(f"{width}x{height}+{x}+{y}")
