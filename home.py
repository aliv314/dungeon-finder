from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
importTest = Blueprint("importTest", __name__, static_folder="static", template_folder='templates')

#Test method to see if database is connected

@importTest.route('/', methods=('GET','POST'))
def home():  # put application's code here
    return render_template("home_page.html")

