from flask import Flask, render_template_string, request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash #Inlcuded within flask, for hashing passwords
import subprocess as sp
import os

#start/stop launches the main hybrid script.
#Start/stop Enables/ Disbales streaming

#======================= Paths =============================
# Get the folder where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Relative path to the other script or file
script_path = os.path.join(BASE_DIR, r"tasks\hybrid.py")

stop_flag = os.path.join(BASE_DIR, r'stop.flag')

EN_CAM = os.path.join(BASE_DIR, r'temp\EN_CAM.flag')
EN_REC = os.path.join(BASE_DIR, r'temp\EN_REC.flag')


#On Boot remove the flags:
if os.path.exists(EN_CAM):
    os.remove(EN_CAM)
if os.path.exists(EN_REC):
    os.remove(EN_REC)

#=========================================================
proc = None
#Create the app object to build the endpoints on
app = Flask(__name__)

app.secret_key = 'Aophf98760AFE9y9fe' #Keeps track fo session, would be randomly generated???

USERS = {
    'admin' : 'scrypt:32768:8:1$7lVZgh6EMX9vD4E2$9829249d3041736b83b6b17fe22451220493c32044603a775109087cac254e5e4af2baeb06b7a8120b3a6f022a3ab38e29bad557bc5fb0afa50aa010b098b5ac',
}
#Convert this to a new password and use enviornment variables on actual computer!

@app.route('/')
def root():
    return redirect('/login')
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        user_pass_hash = USERS.get(u)
        
        if user_pass_hash and check_password_hash(user_pass_hash, p):
            session['user'] = u 
            return redirect('/dashboard')
        return render_template('InvalidCred.html')
    return render_template('login.html')
    

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
        
    return redirect('/login')


    
@app.route('/toggle-stream', methods=['POST'])
def toggleStream():

    #Check Condition of stream
    if os.path.exists(EN_CAM):
        os.remove(EN_CAM)
        return redirect('/dashboard')
        
    else:
        with open(EN_CAM, 'w') as f:
            f.write('EN_CAM')
        return redirect('/dashboard')
        
@app.route('/toggle-record', methods=['POST'])
def toggleRecording():
    #Check Condition of stream
    if os.path.exists(EN_REC):
        os.remove(EN_REC)
        print("Stopping Recording...")
        return redirect('/dashboard')
        
    else:
        with open(EN_REC, 'w') as f:
            f.write('EN_REC')
        print("Starting Recording...")
        return redirect('/dashboard')
    
    
if __name__ == '__main__':
    #Start program for managing stream and recording!
    proc = sp.Popen(["py", script_path])
    #Start Webserver
    app.run(host='0.0.0.0',port=5000)

