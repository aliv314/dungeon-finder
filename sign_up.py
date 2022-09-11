from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint, session
from pymongo import MongoClient
import bcrypt
from home import importTest

signUp = Blueprint("signUp", __name__, static_folder="static", template_folder='templates')

#Connects the login to the Database
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
gameinfo = db.gameinfo

@signUp.route('/sign-up', methods=('GET','POST'))
def sign_up():
    if request.method=='POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        
        #Checks to see if a user is creating an account using existing credentials. Also checks to make sure password is input correctly
        user_found = records.find_one({'username': username})
        email_found = records.find_one({'email': email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('sign_up.html', message=message)
        if email_found:
            message = 'This email already is already taken'
            return render_template('sign_up.html', message=message)
        if password != confirmPassword:
            message = 'Both passwords must match'
            return render_template('sign_up.html', message=message)
        
        #If all the condtions are checked, stores the passed info in the database, hashing the password
        else:
            hashed = bcrypt.hashpw(confirmPassword.encode('utf-8'), bcrypt.gensalt())
            user_input = {'username': username, 'email': email, 'password': hashed}
            records.insert_one(user_input)

    return render_template("sign_up.html")
