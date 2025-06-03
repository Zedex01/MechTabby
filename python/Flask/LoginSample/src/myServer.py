from flask import Flask, render_template_string, request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash #Inlcuded within flask, for hashing passwords

#Create the app object to build the endpoints on
app = Flask(__name__)

app.secret_key = 'Aophf98760AFE9y9fe' #Keeps track fo session, would be randomly generated???

USERS = {
    'admin' : 'scrypt:32768:8:1$7lVZgh6EMX9vD4E2$9829249d3041736b83b6b17fe22451220493c32044603a775109087cac254e5e4af2baeb06b7a8120b3a6f022a3ab38e29bad557bc5fb0afa50aa010b098b5ac',
}

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        user_pass_hash = USERS.get(u)
        
        if check_password_hash(user_pass_hash, p):
            session['user'] = u 
            return redirect('/dashboard')
        return "Invalid credentials. <a href='/login'>Try again</a>"
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')



@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome, {session['user']}! <a href='/logout'>Logout</a>"
    return redirect('/login')


    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

