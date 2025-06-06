#Sample Stream program

from flask import Flask, Response, render_template_string
import cv2


#Initialize Flask app
app = Flask(__name__)

#Open default webcam (0 = default)
cap = cv2.VideoCapture(0)

#Generator function that captures videoframes and yields them as JPEG byte data
def gen_frames():
    while cap.isOpened():
        success, frame = cap.read() #Capture a frame from this camera
        
        if success:
            #encode frame as JPEG
            _ , buffer = cv2.imencode('.jpg', frame) #_ is the return value, ie was it succesfull.
            frame = buffer.tobytes()
            
            #Yield frame in multipart format. This is what browsers deal with for MPEG streams
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break   #Exit if the frame cannot be read

#Endpoint provides the videostream as an http response.
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


#How to use it in html
@app.route('/live')
def index():
    return render_template_string('''
        <html>
        <body>
            <h1>Live Video</h1>
            <img src="{{url_for('video_feed')}}">
        </body>
        </html>
    
    ''')
    
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)