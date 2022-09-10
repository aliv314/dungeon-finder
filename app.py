from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("home_page.html")


if __name__ == '__main__':
    app.run(debug=True)
