from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
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
            return "x wins"
        if state[row] == ["o", "o", "o"]:
            return "o wins"
        if state[0][row] == state[1][row] == state[2][row] != "-":
            return state[0][row] + " wins"
    if state[0][0] == state[1][1] == state[2][2] != "-":
        return state[0][0] + " wins"
    if state[0][2] == state[1][1] == state[2][0] != "-":
            return state[0][2] + " wins"
    for row in range(0,3):
        for column in range(0,3):
            if state[row][column] == "-":
                return "Keep playing"
    return "It's a tie"

@app.route('/game', methods=['GET', 'POST'])
def game():
    global state
    global turn
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
                else:
                    turn = "x"
            else:
                error = "Position was taken"
                status_code = 400
    win = check_win(state)
    return render_template('tictactoe.html', state=state, error=error, win=win), status_code