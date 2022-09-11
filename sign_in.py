from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint
from pymongo import MongoClient
import bcrypt
   
login = Blueprint("login", __name__, static_folder="static", template_folder='templates')

#Connects the login to the Database
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
gameinfo = db.gameinfo
   
@login.route('/sign-in', methods=('GET','POST'))
def sign_in():  # put application's code here
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password'] 

        #Checks to see if a user is creating an account using existing credentials. Also checks to make sure password is input correctly
    user_found = records.find_one({'username': username})
    if user_found:
        message = 'There already is a user by that name'
        return render_template('sign_up.html', message=message)

    return render_template("sign_up.html")