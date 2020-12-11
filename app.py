import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from API.requests_api import RequestsApi
from models.Vote import Vote
import random

app = Flask(__name__)
app.secret_key = "abcde12345"

def session_validate():
    if 'login' in session:
        return True
    else:
        return False

@app.route('/')
def index():
    if session_validate() == False:
        return redirect(url_for('login'))

    res = RequestsApi.get_all_api()
    return render_template('index.html', votes = res)


@app.route('/new')
def new():
    if session_validate() == False:
        return redirect(url_for('login'))
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    if session_validate() == False:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            imglist = ['12d', '7hv', '47c', 'MTkwMTA4Mw', '2fd', 'ORMN4W_9X']
            img = random.choice(imglist)
            value_input = request.form['value_input']
            vote = Vote(value=int(value_input), image_id=img)
            res = RequestsApi.save_api(vote)
            flash('Vote saved')
            return redirect(url_for('index'))
        except:
            flash('Not saved')

@app.route('/view/<id>')
def view(id):
    if session_validate() == False:
        return redirect(url_for('login'))

    res = RequestsApi.get_one_api(id)
    return render_template('view.html', vote = res)

@app.route('/delete/<id>')
def delete(id):
    if session_validate() == False:
        return redirect(url_for('login'))

    res = RequestsApi.delete_api(id)
    flash('Element deleted')
    return redirect(url_for('index'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if session_validate() == True:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            if(username == 'sza95'):
                if(password == '123456789'):
                    session['login'] = True
                    session['username'] = username
                    return redirect(url_for('index'))
                else:
                    flash('Wrong Password')  
            else:
                flash('User not found')  
        except:
            flash('Connection Error')  

    return render_template('login.html')


@app.route('/logout')
def logout():
    if session_validate() == False:
        return redirect(url_for('login'))
    session.pop('login', None)
    session.pop('username', None)

    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=7600, debug=True)