from pathlib import Path
import win32com.client
import time, random
import subprocess, os, urllib.parse
class Selector:
    def __init__(self):
        self.c_path = Path(r'C:\Users\mmoran\Desktop\Sandbox\C\Point Clouds')
        self.d_path = Path(r'C:\Users\mmoran\Desktop\Sandbox\D\Point Clouds')

        #self.path = Path(r'C:\Users\mmoran\Desktop\Sandbox')
        self.dir_list = []
        self.sn_paths = []
        self.total_files = 1
    
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
    def gen_list(self):
        self.dir_list = []
        for i in range(75):
            self.dir_list.append(str(random.randint(190000,190400)))
    
    #Can be called to add a list of dir to be added to the internal list
    def add_to_list(self, list) -> None:
        #print("Appending To List")
        self.dirs_list = []

        for line in list:
            self.dir_list.append(line.strip())


    def find_sn_paths(self, c_path, sn_list):
        #return list of path objects for src files
        self.sn_paths = []
        for root, dirs, files in os.walk(c_path):
            for d in dirs:
                if d in sn_list:
                    self.sn_paths.append(Path(root) / d)

    #Generates a new dst path with same structre as source
    def get_dst_path(self, src_path, c_base, d_base):
        relative = src_path.relative_to(c_base)
        print(f"Dst: {d_base / relative}")
        return d_base / relative


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

            subprocess.run([
            "robocopy",
            str(sn_path),
            str(dst_path),
            "/E",
            "/MOVE",
            "/R:0",
            "/W:0",
            "/MT:16",
            "/NFL",
            "/NDL",
            ])
            files_moved += 1

            if popup:
                popup.after(0, lambda m=files_moved: popup.update_progress(m))

        if popup and not popup.cancelled:
            popup.after(0,popup.destroy())

    
    def filter_dirs(self):
        if len(self.dir_list) > 0:
            #Wrap in ''
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


#sel = Selector()
#sel.move_folders()
#sel.gen_list()
#sel.filter_dirs()