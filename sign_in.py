from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint, session
from pymongo import MongoClient

   
login = Blueprint("login", __name__, static_folder="static", template_folder='templates')

#Connects the login to the Database
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
gameinfo = db.gameinfo
   
@login.route('/', methods=('GET','POST'))
def sign_in():  # put application's code here
    if request.method=='POST':
        if "email" in session:
            email = session['email']
            return render_template('sign_in.html', email=email)
        else:
            return redirect(url_for(sign_in))

    return render_template("sign_up.html")