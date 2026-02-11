from pathlib import Path
import win32com.client
import time, random
import subprocess, os, urllib.parse
from util.Config import Config
from util.SevenZip import SevenZip

#For Popup
import ctypes

MB_OK = 0x00000000
MB_ICONERROR = 0x00000010
MB_TASKMODAL = 0x00002000  # blocks interaction with the current app

class Selector:
    def __init__(self):
        self.cfg = Config()
        self.c_path = Path(self.cfg.get_str("paths", "c_pcl"))
        self.d_path = Path(self.cfg.get_str("paths", "d_pcl"))
        self.core_count = self.cfg.get_str("move-settings", "multi-thread-core-count")
        #self.c_path = Path(r'C:\Users\mmoran\Desktop\Sandbox\C\Point Clouds')
        #self.d_path = Path(r'C:\Users\mmoran\Desktop\Sandbox\D\Point Clouds')
        self.dir_list = []
        self.sn_paths = []
        self.total_files = 1
        self.d_sn_paths = []
        
    
#getters/setters
    def set_path(self):
        pass

    def get_path(self):
        return self.path

    def get_total_files(self):
        self.find_sn_paths(self.c_path, self.dir_list)
        self.total_files = len(self.sn_paths)
        return self.total_files

#functions
    #Can be called to add a list of dir to be added to the internal list
    def add_to_list(self, list) -> None:
        #print("Appending To List")
        self.dirs_list = []

        for line in list:
            self.dir_list.append(line.strip())

    #Gets the full path for each of the serial Numbers
    def find_sn_paths(self, c_path, sn_list):
        #return list of path objects for src files
        self.sn_paths = []
        for root, dirs, files in os.walk(c_path):
            for d in dirs:
                if d in sn_list:
                    self.sn_paths.append(Path(root) / d)

    def find_d_sn_paths(self, d_path, sn_list):
        self.d_sn_paths = []
        print(f"Starting Walk of: {d_path}\n Using: {sn_list}")
        for root, dirs, files in os.walk(d_path):
            print(root)
            for d in dirs:
                print(f"{root} {d}")
                if d in sn_list:
                    print(f"found {d}")
                    self.d_sn_paths.append(Path(root) / d)
                    print(Path(root) / d)

    #Generates a new dst path with same structure as source
    def get_dst_path(self, src_path, c_base, d_base):
        relative = src_path.relative_to(c_base)
        print(f"Dst: {d_base / relative}")
        return d_base / relative

    #Move Folders
    def move_folders(self, popup=None):
        if not self.c_path.exists() or not self.d_path.exists():
            print("ERR: Invalid paths")
            return

        #Find all files that need to be moved
        self.find_sn_paths(self.c_path, self.dir_list)
        self.total_files = len(self.sn_paths)

        if self.total_files == 0:
            print("Nothing to move")
            return
        
        files_moved = 0
        for sn_path in self.sn_paths:

            if popup and popup.cancelled:
                print("Move Canceled")
                return

            dst_path = self.get_dst_path(sn_path, self.c_path, self.d_path)
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            self.core_count = self.cfg.get_str("move-settings", "multi-thread-core-count")
            print(f"Active Cores: {self.core_count}")

            subprocess.run([
            "robocopy",
            str(sn_path),
            str(dst_path),
            "/E",
            "/MOVE",
            "/R:0",
            "/W:0",
            f"/MT:{self.core_count}",
            "/NFL",
            "/NDL",
            ])
            files_moved += 1

            if popup:
                popup.after(0, lambda m=files_moved: popup.update_progress(m))

        if popup and not popup.cancelled:
            popup.after(0,popup.destroy())


    def zip_files(self):
        if len(self.dir_list) > 0:
            print("List contains content")
            self.find_d_sn_paths(self.d_path, self.dir_list)
            
            if len(self.d_sn_paths) > 0:
                print(f"Found {len(self.d_sn_paths)} Parts. Attempting to zip")
                
                #Build the zip command and return to main thread
                #print(self.d_sn_paths)
                sz = SevenZip(self.d_sn_paths)
                #sz.build_archive()
                sz.build_cmd()
                return sz.get_cmd()

            else:
                print("Could not find paths")
                #Display a popup window to the user
                ctypes.windll.user32.MessageBoxW(0, "No pointclouds found.", "AutoZipper", MB_OK | MB_ICONERROR | MB_TASKMODAL)
                return None



    def filter_dirs(self):
        
        if len(self.dir_list) > 0:

            encoded_names = [urllib.parse.quote(f'"{name}"') for name in self.dir_list]

            if len(self.dir_list) > 1:
                search_query = "%20OR%20".join(encoded_names) + "%20kind:folders"
            else:
                search_query = self.dir_list[0]  + "%20kind:folders"

            search_uri = f'search-ms:query={search_query}&crumb=location:{self.d_path}'
            # Open Explorer with search query
            os.startfile(search_uri)

        else:
            print("Err: No Serial Numbers provided")

