from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = 'This is a secret'

@app.route('/')
def numberGame():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    if 'num_guess' not in session:
        session['num_guess'] = 0
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    session['num_guess'] += 1
    session['user_guess'] = int(request.form['user_guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')

if (__name__) == '__main__':
    app.run(debug=True)