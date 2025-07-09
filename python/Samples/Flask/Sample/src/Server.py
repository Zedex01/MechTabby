from flask import Flask, render_template_string, request, session, redirect, url_for, render_template

#Create the app object to build the endpoints on
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('homepage.html')
    
@app.route('/layout1')
def layout1():
    return render_template('Layout1.html')

@app.route('/layout2')
def layout2():
    return render_template('Layout2.html')

    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)

