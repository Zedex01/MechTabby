'''
Matthew Moran
Lizard.py
'''

from pynput import keyboard as kb
#from playsound import playsound

from concurrent.futures import *
import subprocess as sp
from tkinter import Tk, messagebox




audio_file = r'D:\\Matt\\Projects\\Git-Repos\\MechTabby\\python\\Lizard\\lizard.wav'

def OnPress(key):
    print(f'Key {key} Pressed')
    if key == kb.Key.space:
        try:
            playsound(audio_file)
        except Exception  as e:
            print(f"ERR: {e}")

def proc():
    print("Playing sound!")
    playsound(audio_file)

def main(argc = None, argv = None):
    print("Starting!")


    with ThreadPoolExecutor(max_workers=32) as executer:
        #futures contains the results of everything
        futures = []
        for i in range(1):
            futures.append(executer.submit(proc))
"""
        for future in as_completed(futures):
            result = future.result()
            print_compact(result)
"""

if __name__ == "__main__":
    main()

