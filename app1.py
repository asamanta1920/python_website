from flask import Flask, render_template, request
import sqlite3
import bcrypt
app = Flask(__name__)

conn = sqlite3.connect("rsvp.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS guests(
    name                  TEXT          NOT NULL,
    email                 VARCHAR(100)  NOT NULL UNIQUE, 
    phone                 NUMBER        NOT NULL,
    num_guests            NUMBER        NOT NULL,
    CHECK(email LIKE '%@%.%') 
)
""")

conn.commit()

@app.route('/')
@app.route('/rsvp', methods=['GET','POST'])

def rsvp():
    if request.method == 'GET':
        status = "Please fill in all the feilds"
    else:
        if len(request.form['phone']) != 10:
            status = "Invalid phone number"
        else:
            cursor.execute("INSERT INTO guests (name, email, phone, num_guests) VALUES (?, ?, ?, ?)", (request.form['name'], request.form['email'],request.form['phone'], request.form['num_guests']))
            conn.commit()
            status = "Your RSVP was sent. Thank you!"
    return render_template('rsvp.html', status = status)

@app.route('/myguests')

def myguests():
    my_guests = cursor.execute("SELECT * from guests")
    return render_template('my_guests.html', info = my_guests.fetchall())