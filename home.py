from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)

importTest = Blueprint("importTest", __name__, static_folder="static", template_folder='templates')

#setup mongodb 
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
gameinfo = db.gameinfo

#Test method to see if database is connected

@importTest.route("/sign-up")
def sign_up():
    return render_template(sign_up.html)

@importTest.route('/', methods=('GET','POST'))
def home():  # put application's code here
    if request.method=='POST':
        content = request.form['content']
        return redirect(url_for('home'))

    return render_template("home_page.html")


    @app.route('/sign-in', methods=('GET','POST'))
    def login():  # put application's code here
        if request.method=='POST':
            username = request.form['username']
            password = request.form['password'] 

        #Checks to see if a user is creating an account using existing credentials. Also checks to make sure password is input correctly
        user_found = records.find_one({'username': username})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('sign_up.html', message=message)
        

        #If all the condtions are checked, stores the passed info in the database, hashing the password
        else:
            user_input = {'username': username, 'email': email, 'password': hashed}
            records.insert_one(user_input)


        return redirect(url_for('signUp'))
    return render_template("sign_up.html")