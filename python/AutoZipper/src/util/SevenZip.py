import sys, os, re
import subprocess as sp
from pathlib import Path
import threading


class SevenZip:
    def __init__(self, files):
        self.files = files
        self.seven_zip_path = r'C:/Program Files/7-Zip/7z.exe'
        self.archive_path = r'C:/Point Clouds/Archive.7z'
        
        self.volumes = True
        self.volume_size_mb = "1000"

        self.cmd = []


# ==== Functions ====
    def build_archive(self):
        #Create command
        self.cmd = [self.seven_zip_path, "a", str(self.archive_path)]
        self.cmd.extend(self.files)

        #If Volumes is true, enable them of size defined
        if self.volumes:
            self.cmd.append(f"-v{self.volume_size_mb}m")

        #Show Progress in cmd
        self.cmd.extend(["-bsp1", "-bso1"])

        self.proc = sp.Popen(self.cmd, text=True, creationflags=sp.CREATE_NEW_CONSOLE)


# === Getters & Setters ===
    
    def set_files(self, files) -> None:
        self.files = files
    
    def get_files(self) -> list:
        return self.files

    def set_volumes(self, use_volumes: bool)-> None:
        self.volumes = use_volumes

    def get_volumes(self) -> bool:
        return self.volumes
    
    def set_volume_size_mb(self, mb) -> None:
        self.volume_size_mb = mb

    def get_volume_size_mb(self) -> int:
        return self.volume_size_mb

