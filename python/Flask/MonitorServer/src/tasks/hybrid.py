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

#Get Path
if config['RECORDING'].getboolean('use_env'):
    #Get Path from system variables
    output_dir = os.environ.get('RECORDING_PATH')
       
else:
    #Get path from config file
    output_dir = config.get('RECORDING','path',fallback=None)

#Verify path 
if output_dir is None:
    print("Please set your recording path!")
    sys.exit()

#Ensure output dir exists
os.makedirs(os.path.dirname(output_dir), exist_ok=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#================Flags==================
EN_CAM = os.path.join(BASE_DIR, r'..\temp\EN_CAM.flag')
EN_REC = os.path.join(BASE_DIR, r'..\temp\EN_REC.flag')


#==================Setup==========================
#Create the capture device, 0 is the default (integrated webcam.)
cap = cv2.VideoCapture(2)

#==================Stream-Config==================
#Create Webserver app
app = Flask(__name__)


#==================Record-Config==================
#Define the codec and create a videowriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')



cap = None
out = None
frame_lock = threading.Lock()
current_frame = None
camWidth = 0
camHeight = 0
#==================Main===========================
def handle_recording():
    global cap, out, current_frame, camHeight, camWidth
    
    while True:
        #Is streaming enabled???
        if os.path.exists(EN_CAM):
        
            #If the camera is not on, enable it
            if cap is None or not cap.isOpened():
                cap = cv2.VideoCapture(0)
                camWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                camHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                print(f"Native resolution: {int(camWidth)} x {int(camHeight)}")
            
            #Read a frame from the camera
            success, frame = cap.read()
            
            #If it did not successfuly capture a frame, skip this itteration.
            if not success:
                continue
            
            #Set the frame captured as the current frame
            with frame_lock:
                current_frame = frame.copy()
            
            #Check if the Enable recording flag exists
            if os.path.exists(EN_REC):
                
                #Check if out has been initialized
                if out is None:
                    dt = datetime.now()
                    dt = dt.strftime("%Y%m%d-%H%M%S")
                    dt = dt + '.mp4'
                    output_path = os.path.join(output_dir, dt)
                    
                    #Ensure the output directory is valid 
                    os.makedirs(os.path.dirname(output_path), exist_ok = True)
                    #Setup the output config from the videowriter
                    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(camWidth),int(camHeight)))
                
                #Write frame to file
                out.write(frame)

            #If there is no Enable Recording flag, but out still exists, release output writer.
            elif out:
                out.release()
                out = None
        
        #If Streaming is not enabled, release all resources
        else:
            time.sleep(0.05)
            
            if cap and cap.isOpened():
                cap.release()
                cap = None
                
            if out:
                out.release()
                out = None
            
            
            
def gen_frames():
    #only while Enable cam flag exists...
    while True:
        if not os.path.exists(EN_CAM):
            time.sleep(0.1)
            continue
            
        with frame_lock:
        
            #if the current_frame has not been set, skip this itteration
            if current_frame is None:
                continue

            _ , buffer = cv2.imencode('.jpg', current_frame) #_ is the return value, ie was it succesfull.
        frame = buffer.tobytes()
            
            #Yield frame in multipart format. This is what browsers deal with for MPEG streams
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
              
        time.sleep(0.05)
        
        
    
            
#Endpoint provides the videostream as an http response.
@app.route('/video_feed')
def video_feed():
    if os.path.exists(EN_CAM):
        return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "Streaming is disabled.", 403


if __name__ == '__main__':
    threading.Thread(target=handle_recording, daemon=True).start()
    app.run(host='0.0.0.0', port=8080)
