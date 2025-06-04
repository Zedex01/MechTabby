import cv2, sys, os, time
from flask import Flask, Response
import threading

#==============CONFIG====================
output_path = r'C:/Users/mmoran/Videos/Recording.mp4'

#Ensure output dir exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
stop_flag = os.path.join(BASE_DIR, r'..\stop.flag')

#Create the capture device, 0 is the default (integrated webcam.)
cap = cv2.VideoCapture(0)


#==================Recording==================
#Define the codec and create a videowriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640,480))


print(f"Recording to: {output_path}")

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
            
        if os.path.exists(stop_flag):
            print("Stop Flag Detected!")
            os.remove(stop_flag)
            print("Removed old flag")
            break
            
            
        time.sleep(0.05)
        
except KeyboardInterrupt:
    print("Recording Stopped Manually")
finally:
    cap.release()
    out.release()
    print("Resources released")

