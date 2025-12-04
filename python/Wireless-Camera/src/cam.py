import cv2, threading, datetime, time
from pathlib import Path

"""
init
Record
Stop?



"""

class Cam:
    def __init__(self, camera: int = None):
        self.recording = False
        self.camera = camera or 0

        self.output_dir = Path(r'D:/Matt/Recordings/WiFi-Cam/')

        self.file_name = None
        self.cam_thread = None
        self.output = None
        self.cap = None


    def set_camera(self, camera):
        self.camera = camera


    def start_recording(self):
        #Don't start a new recording if already recording
        if self.recording or not self.cam_thread is None:
            print("Already recording!")
            return
        
        print("Starting Recording...")
        
        print("Setting file name to: ", end = "")
        #Get Current Time, use as file name
        ts = datetime.datetime.now()
        tsf = ts.strftime("%Y-%m-%d_%H-%M-%S")
        self.file_name = f"Capture_{tsf}.avi"
        print(self.file_name)
        self.file_path = self.output_dir / self.file_name

        # === Setup Capture ===

        print("Opening Camera...")
        #Check Cam is accessable
        self.cap = cv2.VideoCapture(self.camera)

        if not self.cap.isOpened():
            print("ERR: Unable to open camera.")
            return
        
        frame_height = int(self.cap.get(4))
        frame_width = int(self.cap.get(3))

        print("Setting up VideoWriter...")
        #Setup Output
        self.output = cv2.VideoWriter(
            str(self.file_path),
            cv2.VideoWriter_fourcc('M','J','P','G'),
            20, #FPS
            (frame_width, frame_height)
        )

        self.recording = True
        self.cam_thread = threading.Thread(target=self._record)
        
        print("Starting Thread...")
        self.cam_thread.start()
        print("Thread Started!")
    

    def stop_recording(self):
        print("Stopping Recording...")

        if not self.recording:
            print("Camera is not recording")
            return
        
        #End recording and wait for thread to join
        self.recording = False
        self.cam_thread.join()
        self.cam_thread = None
        print("Recording Finished!")
        

    #Function for thread
    def _record(self):
        while self.recording:

            ret, frame = self.cap.read()

            if not ret:
                print("failed to grab frame")
                break 
            
            #Write frame to file
            self.output.write(frame)

        #Release Stuff
        self.output.release()
        self.cap.release()
        

if __name__ == "__main__":
    cam = Cam()
    cam.start_recording()
    print("waiting 15 seconds...")
    time.sleep(15)
    cam.stop_recording()
