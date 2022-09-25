from flask import Flask, render_template, session

from create_party import party
from home import home_page
from sign_up import signUp
from sign_in import login

app = Flask(__name__)
app.register_blueprint(home_page, url_prefix="/")
app.register_blueprint(signUp, url_prefix="/signup")
app.register_blueprint(login, url_prefix="/signin")
app.register_blueprint(party, url_prefix="/create_party")

#Tests to make sure blueprint is routing properly 
@app.route("/")
def test():
    return "<h1>test</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)
