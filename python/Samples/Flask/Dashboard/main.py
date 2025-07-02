from flask import Flask, render_template_string, request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash #Inlcuded within flask, for hashing passwords

#Create the app object to build the endpoints on
app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

