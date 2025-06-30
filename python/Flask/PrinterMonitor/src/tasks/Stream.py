"""
2025 06 01

Subprocess that handles both streaming and recording at the same time
"""
#=============IMPORTS====================
import cv2, sys, os, time, threading, configparser
from flask import Flask, Response
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#==============CONFIG====================
config_file = os.path.join(BASE_DIR, r'../config.ini')
config = configparser.ConfigParser()

#Check for config file
ret = config.read(config_file)
if not ret:
    print('config.ini not found! please add your config file.')
    sys.exit()

#Get path from config file
VideoCaptureDevice = int(config.get('SETUP','device',fallback=0))
print(VideoCaptureDevice)
if VideoCaptureDevice == 0:
    print("Using Default Camera")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#================Flags==================
EN_CAM = os.path.join(BASE_DIR, r'..\temp\EN_CAM.flag')

#==================Setup==========================
#Create the capture device, 0 is the default (integrated webcam.)
#cap = cv2.VideoCapture(VideoCaptureDevice)
#stream_lock = threading.Lock() #For preventing multiple instances of gen_frames

#==================Stream-Config==================
#Create Webserver app
app = Flask(__name__)


#==================Main===========================
def gen_frames():
    print("Running Gen Frames!")
    cap = None
    #only while Enable cam flag exists...
    while True:
        if not os.path.exists(EN_CAM):
            if cap: #If it is after running, release cam and break loop
                cap.release()
                cap = None
                print("Cam Released")
                break
            continue
        
        if cap is None:
            print("Turning On Cam...")
            cap = cv2.VideoCapture(VideoCaptureDevice)

        success, frame = cap.read()

        if success:
            _ , buffer = cv2.imencode('.jpg', frame) #_ is the return value, ie was it succesfull.
            frame = buffer.tobytes()
            
            #Yield frame in multipart format. This is what browsers deal with for MPEG streams
            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#Endpoint provides the videostream as an http response.
@app.route('/video_feed')
def video_feed():
    if os.path.exists(EN_CAM):
        return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "Streaming is disabled.", 403

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)