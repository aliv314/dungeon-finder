from flask import Flask, redirect, url_for, render_template, request, redirect, flash
from pymongo import MongoClient
import bcrypt
import requests

app = Flask(__name__)

#setup mongodb 
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
gameinfo = db.gameinfo

#Grabs the Game Name and Images through API calls
api_image = 'https://api.boardgameatlas.com/api/game/images?limit=20&client_id=BPsyAhFgcY'
imageCall = requests.get(api_image).json()
imageTest = imageCall['images'][0]['url']
gameID = imageCall['images'][0]['game']['id']
api_name = 'https://api.boardgameatlas.com/api/search?ids={0}&client_id=BPsyAhFgcY'.format(gameID)
nameCall = requests.get(api_name).json()
gameName = nameCall['games'][0]['name']

print(imageTest)
print(gameName)


#Test method to see if database is connected
records.count_documents({})

@app.route('/', methods=('GET','POST'))
def home():  # put application's code here
    if request.method=='POST':
        content = request.form['content']
        return redirect(url_for('home'))

    return render_template("home_page.html")

@app.route('/sign-up', methods=('GET','POST'))
def signUp():  # put application's code here
    #passes all the information from the POST method in sign_up
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


        return redirect(url_for('signUp'))
    return render_template("sign_up.html")

if __name__ == '__main__':
    app.run(debug=True)
