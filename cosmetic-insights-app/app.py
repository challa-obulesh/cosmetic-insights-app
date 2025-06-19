
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('dashboard1'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/dashboard3')
def dashboard3():
    return render_template('dashboard3.html')

@app.route('/dashboard4')
def dashboard4():
    return render_template('dashboard4.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
