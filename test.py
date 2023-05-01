from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
import psycopg2
import psycopg2.extras
from datetime import datetime
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://contact_query_databse_user:SYWt3zrIo3aEjJDqwcxemqaz6HuMMmkU@dpg-ch5l8s5269v5rfrcrp50-a/contact_query_databse"

#postgresql://contact_query_databse_user:SYWt3zrIo3aEjJDqwcxemqaz6HuMMmkU@dpg-ch5l8s5269v5rfrcrp50-a.oregon-postgres.render.com/contact_query_databse

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'You cant guess this key'

db = SQLAlchemy(app)

class Response(db.Model):
    __tablename__ = "Form_Response"
    name = db.Column(db.String[30])
    email = db.Column(db.String[30], primary_key=True)
    subject = db.Column(db.String[40])
    message = db.Column(db.String[500])
    data = db.Column(db.Integer)

    def __init__(self, nm, em, sub, mess, da):
        self.name = nm
        self.email = em
        self.subject = sub
        self.message = mess
        self.data = da

@app.route('/', methods=["GET", "POST"])
def portfolio():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def contact_info():

    email = None
    # if request.method == "POST":
    #     email = request.form['email']
    #     name = request.form['name']
    #     subject = request.form['subject']
    #     message = request.form['message']
    #     date = datetime.now()
    #     try:
    #         con = psycopg2.connect('postgresql://contact_query_databse_user:SYWt3zrIo3aEjJDqwcxemqaz6HuMMmkU@dpg-ch5l8s5269v5rfrcrp50-a.oregon-postgres.render.com/contact_query_databse')
    #         c = con.cursor()
    #         c.execute("INSERT INTO Form_Response (name,email,subject,message,date) VALUES(?,?,?,?,?)",(name,email,subject,message,date))
    #         con.commit()
    #         flash("Thank you for contacting me, I will get back to you as soon as possible")
    #         render_template('index.html', email=email)
    #     finally:
    #         con.close()
    if request.method == "POST":
        email = request.form['email']
        name = request.form['name']
        subject = request.form['subject']
        message = request.form['message']
        date = datetime.now()

        form_response = Response(name, email, subject, message, date)
        db.session.add(form_response)
        db.session.commit()


    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)