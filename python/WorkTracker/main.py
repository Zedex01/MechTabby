from src.SimpleSQL import SimpleSQL
import src.PathManager as pm
import tkinter as tk
from tkinter import messagebox

def main():
    #info_popup(f"Base Path: {pm.get_base_path()}\nDB Path: {pm.get_database_path()}\nConfig Path: {pm.get_config_path()}")

    #Create simpleSQL instance and try to connect
    sql = SimpleSQL(pm.get_database_path())
    
    #sql.create_table()

    sql.add_entry("2026-01-22", "Autotool", 4.0, None, "Office", "Assisting Chris & Dean, Troubleshooting old system network issues.")

    #tables = sql.get_tables()
    #print(tables)
    #print("DATA:")
    #sql.get_all()



def info_popup(text):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Information", text)
    root.destroy()


if __name__ == "__main__":
    main()