from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<username>')
def hello_world(username = None):
    print(username)
    return render_template('hello.html', name = username)