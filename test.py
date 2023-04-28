from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'You cant guess this key'

db = SQLAlchemy(app)

con = sql.connect('messages.db')
con.execute('CREATE TABLE IF NOT EXISTS Form_Response (ID INTEGER PRIMARY KEY AUTOINCREMENT,'+'name TEXT,email TEXT,subject TEXT,message TEXT,date TEXT)')

con.close()

@app.route('/', methods=["GET", "POST"])
def portfolio():
    return render_template('index.html')

@app.route('/contact_info', methods=["GET", "POST"])
def contact_info():
    email = None
    if request.method == "POST":
        email = request.form['email']
        name = request.form['name']
        subject = request.form['subject']
        message = request.form['message']
        date = datetime.now()
        try:
            con = sql.connect('messages.db')
            c = con.cursor()
            c.execute("INSERT INTO Form_Response (name,email,subject,message,date) VALUES(?,?,?,?,?)",(name,email,subject,message,date))
            con.commit()
            flash("Thank you for contacting me, I will get back to you as soon as possible")
            render_template('index.html', email=email)
        finally:
            con.close()


    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)