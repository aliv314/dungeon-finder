from flask import Flask, redirect, url_for, render_template
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config["MONGO_URI"] = "mongodb+srv://tinky:<password>@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority"

#setup mongodb 
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
def home():  # put application's code here
    return render_template("sign_up.html")

if __name__ == '__main__':
    app.run(debug=True)
