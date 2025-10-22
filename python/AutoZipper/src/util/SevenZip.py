import sys, os, re
import subprocess as sp
from pathlib import Path
import threading
from util.Config import Config
from datetime import datetime


class SevenZip:
    def __init__(self, files):
        self.files = files
        self.seven_zip_path = r'C:/Program Files/7-Zip/7z.exe'
        #self.archive_path = r'C:/Point Cloud Archives/Archive.7z'

        self.cfg = Config()
        self.archive_root = Path(self.cfg.get_str("paths", "output_path"))

        self.volumes = True
        self.volume_size_mb = "1000"

        self.cmd = []


# ==== Functions ====
    def build_archive(self):
        now = datetime.now().strftime("%Y%m%d-%H%M%S")

        #Create Archive Dir
        archive_dir = self.archive_root / now
        archive_dir.mkdir(parents=True, exist_ok=True)

        archive_name = f"Archive-{now}.7z"
        archive_path = archive_dir / archive_name

        #Create command
        self.cmd = [str(self.seven_zip_path), "a", str(archive_path)]
        self.cmd.extend(str(f) for f in self.files)

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

