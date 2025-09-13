'''
Matthew Moran
Lizard.py
'''

from pynput import keyboard as kb
from playsound import playsound

audio_file = r'D:\Matt\Projects\Git-Repos\MechTabby\python\Lizard\lizard.wav'

def OnPress(key):
    print(f'Key {key} Pressed')
    if key == kb.Key.space:
        try:
            playsound(audio_file)
        except Exception  as e:
            print(f"ERR: {e}")

with kb.Listener(on_press=OnPress) as listner:
    listner.join()