from flask import Flask, redirect, url_for, render_template, request, redirect, flash, Blueprint, session
import geocoder
from pymongo import MongoClient
import bcrypt
import json

app = Flask(__name__)
g = geocoder.ip('me')

home_page = Blueprint("home_page", __name__, static_folder="static", template_folder='templates')


# Test method to see if database is connected
@home_page.route('/', methods=('GET', 'POST'))
def home():  # put application's code here
    return render_template("home_page.html")


# setup mongodb
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users
party = db.party

@app.route('/', methods=('GET', 'POST'))
def home():  # put application's code here

    lat = g.latlng[0]
    lon = g.latlng[1]
    #db.collection.create_index({ "location": "2dsphere"} )

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
    #Mongo uses longitude, latitude; leaflet uses latitude, longitude, so we flip them.
    """
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
    """
    return render_template("home_page.html")

if __name__ == '__main__':
    home.run(debug=True)
