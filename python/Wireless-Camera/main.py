#Matthew Moran

import socket, cv2, time
from src.cam import Cam

HOST = '0.0.0.0' #Local Host
PORT = 65432 #NOTE: Make sure port is > 1023 to prevent system interferance

#Set how long between motions to keep recording (s)
TIMEOUT = 30

#Start at 0
timer = 0

is_recording = False

#Set inital Tick
last_tick = time.time()

#Set Socket Configuration
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    #Set the Server IP and Port
    socket.bind((HOST,PORT))
    
    serverOnline = True

    #Create Cam object
    cam = Cam()
        
    print(f"======Server Online!======\n Listening @ {HOST}:{PORT}")
    
    while serverOnline:

        socket.listen() #This needs to be in a loop to keep looking for connections even once they are all gone
        
        #Will wait untill it recieves an inbound connection request
        conn,addr = socket.accept()

        #Set Connection Timeout
        conn.settimeout(5) 
        
        #While the connection is established...
        with conn:
            print(f"Connected By: {addr}") #Prints out the inbound connection 
            _connected = True
            
            while _connected:
                try:  
                    #Store recieved information from communication in data
                    data = (conn.recv(53248)).decode('utf-8').strip()

                    #reset timer clock when recv 1 from client
                    if data != "":
                        if data == "1":
                            timer = TIMEOUT
                            continue

                    # === Timer Ticks ===
                    #Get time
                    now = time.time()
                    #if 1 second or more has passed, update timer
                    if now - last_tick >= 1:
                        if timer > 0:
                            timer -= 1
                        print("Time Remaining: ", timer)
                        #Set last tick to be equal to now
                        last_tick = now


                    # === Recording States ===
                    #If not recording and the timer is greater than 0, start recording
                    if not is_recording and timer > 0:
                        is_recording = True
                        print("Server Recording...")
                        cam.start_recording()

                    #If is recording and the timer has expired, stop the recording
                    elif is_recording and timer <= 0:
                        is_recording = False
                        print("Server Stoping Recording!")
                        cam.stop_recording()

                        
                except (ConnectionResetError, TimeoutError):
                    print("Connection reset by peer")
                    break



