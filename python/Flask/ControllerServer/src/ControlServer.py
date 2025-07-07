from flask import Flask, render_template_string, request, session, redirect, url_for, render_template
import os, serial, time


class MockSerial:
    def write(self, data):
        print(f"[MOCK SERIAL] Would send: {data.decode().strip()}")

    def close(self):
        pass

    @property
    def is_open(self):
        return True



#======================= Paths =============================
# Get the folder where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#=========================================================
PORT = 'COM7'
BAUDRATE = 115200
try:
#Mount Serial Port
    ser = serial.Serial(PORT, BAUDRATE)

    time.sleep(2)
except:
    print("No Serial Found, Booting Mock")
    ser = MockSerial()
#==========================================================
"""
====Translation====
| 14 | D-Up       |
| 13 | D-Right    |
| 12 | D-Down     |
| 11 | D-Left     |
| 10 | X          |
| 9  | A          |
| 8  | B          |
| 7  | Y          |
| 6  | LB         |
| 5  | LT         |
| 4  | RT         |
| 3  | RB         |
| 2  | +          | 
| 1  | -          |
| 0  | Home       |
| JU | JS-Up      |
| JN | JS-Net     |
| JD | JS-Down    | 
===================
"""
# Button map (optional for display/future use)
button_map = {
    "d-up": "14",
    "d-right": "13",
    "d-down": "12",
    "d-left": "11",
    "x": "10",
    "a": "9",
    "b": "8",
    "y": "7",
    "lb": "6",
    "lt": "5",
    "rt": "4",
    "rb": "3",
    "+": "2",
    "-": "1",
    "home": "0",
    "ju": "JU",
    "jn": "JN",
    "jd": "JD",    
}


#===== MAIN =====================================================
#Create the app object to build the endpoints on
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('control.html', buttons = button_map)
    
@app.route('/send/<code>')
def send(code):
    # Make sure code is valid
    if code.upper() in [v.upper() for v in button_map.values()]:
        ser.write((code + '\n').encode())
    return redirect('/')
    
    
if __name__ == '__main__':
    #Start Webserver
    app.run(host='127.0.0.1',port=5000, debug=True) #Only Avaliable on localhost

