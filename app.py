from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'ayush' or \
                request.form['password'] != 'ha@bhai':
            error = 'Login unsuccessful-Invalid credentials'
        else:
            flash('You are logged in successfully')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)