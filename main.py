from flask import Flask, render_template
from home import importTest
from sign_up import signUp
from sign_in import login

app = Flask(__name__)
app.register_blueprint(importTest, url_prefix="")
app.register_blueprint(signUp, url_prefix="")
app.register_blueprint(login, url_prefix="")


#Tests to make sure blueprint is routing properly 
@app.route("/")
def test():
    return "<h1>test</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)
