import customtkinter as ctk
import tkinter as tk
from tkinter import ttk


class Application(ctk.CTk): #Application IS a tkinter is an instance
    def __init__(self): #Create a constructor based on super
        super().__init__()

        self.title("Simple App")

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
        else:
            self.toplevel_window.focus() #Focus already existing window
        

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

        self.entry_btn = ctk.CTkButton(self, text="Add", command=self.parent.open_toplevel)
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

        self.title="Custom Popup Window"
        self.geometry("400x300")
        self.label = ctk.CTkLabel(self, text="TopLevelWindow!")
        self.label.pack(padx=20,pady=20)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('blue')

#Create Instance of tkinter
app = Application()

#Start said instance
app.mainloop()
