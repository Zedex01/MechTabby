from src.SimpleSQL import SimpleSQL
import src.PathManager as pm
import tkinter as tk
from tkinter import messagebox

def main():
    #info_popup(f"Base Path: {pm.get_base_path()}\nDB Path: {pm.get_database_path()}\nConfig Path: {pm.get_config_path()}")

    #Create simpleSQL instance and try to connect
    sql = SimpleSQL(pm.get_database_path())
    print("Success")


def info_popup(text):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Information", text)
    root.destroy()


if __name__ == "__main__":
    main()