from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/<username>')

def hello_world(username = None):
    name = username
    print(username)
    return render_template('hello_is_none.html') if not name else render_template('hello1.html', name)