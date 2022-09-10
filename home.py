from flask import Flask, redirect, url_for, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)


#setup mongodb 
client = MongoClient('mongodb+srv://testuser:Q2PYvAxN79Diu5QX@tinkydb.9hvmnek.mongodb.net/?retryWrites=true&w=majority')
db = client.get_database("DungeonFinder")
records = db.users

records.count_documents({})
new_student = {
    'name': 'Winkle',
    'number': 13
}
records.insert_one(new_student)

@app.route('/', methods=('GET','POST'))
def home():  # put application's code here
    if request.method=='POST':
        content = request.form['content']
        return redirect(url_for('home'))
        #users.insert_one({'content': content})
    
    #all.users = users.find()
    return render_template("home_page.html")

if __name__ == '__main__':
    app.run(debug=True)
