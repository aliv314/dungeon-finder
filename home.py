import geocoder
from flask_modals import Modal
from flask import Flask, url_for, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# setup mongodb
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users

"""
records.count_documents({})
new_student = {
    'name': 'Winkle',
    'number': 13
}
records.insert_one(new_student)
"""


@app.route('/', methods=('GET', 'POST'))
def home():  # put application's code here

    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for('home'))

    g = geocoder.ip('me')
    markers = [
        {
            'lat': 0,
            'lon': 0,
            'popup': 'This is the middle of the map.'
        }
    ]
    return render_template("home_page.html",  markers=markers, lat=g.latlng[0], lon=g.latlng[1])


@app.route('/create-party/', methods = ['GET'])
def create():
    print("Clicked create!")
    return render_template("create_party.html")


@app.route('/confirm-party/', methods=(['POST']))
def confirmCreate():

    return None


@app.route('/search-party/', methods=(['GET, POST']))
def search():
    print("Clicked search!")

    return render_template("home_page.html")


if __name__ == '__main__':
    home.run(debug=True)
