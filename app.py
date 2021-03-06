from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import bcrypt
from flask_socketio import SocketIO

app = Flask(__name__)

app.secret_key = b's\x1a\xd3\x13\xac\xef\x1aq\x98Z\xb5%P#\xda\xfa'

socketio = SocketIO(app)
socketio.run(app)

conn = sqlite3.connect("signup.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username              TEXT          NOT NULL UNIQUE,
    name                  TEXT          NOT NULL,
    email                 VARCHAR(100)  NOT NULL UNIQUE, 
    password              TEXT          NOT NULL,
    CHECK(email LIKE '%@%.%') 
)
""")

conn.commit()
conn.close()

@app.route('/hello/<username>')

def hello_world(username = None):
    name = username
    print(username)
    return render_template('hello1.html', name=name)

state = []
turn = "x"

def make_state():
   return [["-" for x in range(0,3)] for y in range(0,3)]

def check_win(state):
    for row in range(0,3):
        if state[row] == ["x", "x", "x"]:
            return "x wins! Game Over! Please don't submit anymore"
        if state[row] == ["o", "o", "o"]:
            return "o wins! Game Over! Please don't submit anymore"
        if state[0][row] == state[1][row] == state[2][row] != "-":
            return state[0][row] + " wins! Game Over! Please don't submit anymore"
    if state[0][0] == state[1][1] == state[2][2] != "-":
        return state[0][0] + " wins! Game Over! Please don't submit anymore"
    if state[0][2] == state[1][1] == state[2][0] != "-":
            return state[0][2] + " wins! Game Over! Please don't submit anymore"
    for row in range(0,3):
        for column in range(0,3):
            if state[row][column] == "-":
                return "Keep playing"
    return "It's a tie"

@app.route('/game', methods=['GET', 'POST'])
def game():
    global state
    global turn
    turn_statement = "It is Player x's turn"
    error = None
    status_code = 200

    if request.method == 'GET':
        state = make_state()
    else:
        position = int(request.form['position']) -1
        print(position) 

        if position < 0 or position > 8:
           error = "Out of bounds"
           status_code = 400
        else:
            row = position // 3
            column = position % 3
            if state[row][column] == "-":

                state[row][column] = turn
                if turn == "x":
                    turn = "o"
                    turn_statement = "It is Player o's turn"
                else:
                    turn = "x"
                    turn_statement = "It is Player x's turn"
            else:
                error = "Position was taken"
                status_code = 400
    win = check_win(state)
    return render_template('tictactoe.html', state=state, error=error, win=win, turn_statement=turn_statement), status_code

@app.route('/signup', methods=['GET','POST'])


def signup():
    global status
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()
    if request.method == 'GET':
        status = "Please fill in all the feilds"
    else:
        if request.form['password'] != request.form['confirm_password']:
            status = "Your confirmed password doesn't match you password. Please enter again."
        else:
            status = "Your information was filled in. Now you can log in."
            hashed = bcrypt.hashpw(request.form['password'].encode("UTF-8"), bcrypt.gensalt())
            try:
                cursor.execute("INSERT INTO users (username, name, email, password) VALUES (?, ?, ?, ?)", (request.form['username'], request.form['name'],request.form['email'], hashed))
                conn.commit()
            except Exception as e:
                print(e)
                status = "An error occured. Signup again later."
    conn.close()
    return render_template('signup.html', status = status)

@app.route('/login', methods=['GET','POST'])

def login():
    global status1
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()
    if request.method == 'GET':
        status1 = "Please fill in all the feilds"
    else:
        try:
            passes = cursor.execute("SELECT password FROM users WHERE username = ?", (request.form['username'],))
            pass_words = passes.fetchone()[0]
            if bcrypt.checkpw(request.form['password'].encode("UTF-8"),pass_words):
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else:
                status1 = "Please enter the login info again. Or sign up for first time user."

        except Exception as error:
            print(error)
            status1 = "Please enter the login info again. Or sign up for first time user."
        
    conn.close()
    return render_template('login.html', status1 = status1)

@app.route('/')
def home():
    if "username" in session:
        return render_template('home.html', username = session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('exit.html')

@app.route('/js')
def js():
    return render_template('js.html')

X = 0
O = 0
T = 0

@app.route('/scoreUpload', methods = ['POST'])
def scoreUpload():
    global X
    global O
    global T

    status = request.form['status']
    if status == "X":
        X += 1
    elif status == "O":
        O += 1
    elif status == "T":
        T += 1
    else:
        return "You provided an invalid score", 400

    print(X, O, T)

    return ""