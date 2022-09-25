from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint, session
from pymongo import MongoClient
import geocoder

party = Blueprint("patrty", __name__, static_folder="static", template_folder='templates')
g = geocoder.ip('me')


#Connects the login to the Database
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
gameinfo = db.gameinfo

@party.route('/create-party')
def create():
    print("Clicked create!")
    if request.method == "POST":
        db.party.insert_one({
            "name": request.form["party-name"],
            "game": request.form["game"],
            "proficiency": request.form["proficiency_select"],
            "location": {
                "coordinates": [g.latlng[0], g.latlng[1]],
                "type": "Point"
            }
        })
    return render_template("create_party.html")