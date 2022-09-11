from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint, session
import geocoder
from pymongo import MongoClient
import bcrypt
import json

app = Flask(__name__)
g = geocoder.ip('me')

importTest = Blueprint("importTest", __name__, static_folder="static", template_folder='templates')


# Test method to see if database is connected
@importTest.route('/', methods=('GET', 'POST'))
def home():  # put application's code here
    return render_template("home_page.html")


# setup mongodb
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
party = db.party

@app.route('/', methods=('GET', 'POST'))
def home():  # put application's code here
    idC = 0
    idd = 'party' + str(idC)
    idC += 1

    lat = g.latlng[0]
    lon = g.latlng[1]
    db.collection.create_index({ "location": "2dsphere"} )

    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for('home'))
    # https://www.mongodb.com/docs/manual/reference/operator/query/near/#behavior
    marked_parties = db.party.find(
        {"location":
            {"$near":
                {"$geometry":
                    {"type": "Point", "coordinates": [lon, lat]}, "$maxDistance":1000
                 }
             }
         })
    markers = []
    # Mongo uses longitude, latitude; leaflet uses latitude, longitude, so we flip them.
    for i in marked_parties:
        markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
                {idd}.addTo(map).bindPopup('{party} <br> {proficiency}');"\
            .format(
            idd=idd,
            latitude=i["location"]["coordinates"][0],
            longitude=i["location"]["coordinates"][1],
            party=i["name"],
            proficiency=i["proficiency"])

    return render_template("home_page.html", markers=markers, lat=lat, lon=lon)


@app.route('/create-party')
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


if __name__ == '__main__':
    home.run(debug=True)
