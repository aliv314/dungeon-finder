from flask import Flask, render_template
from home import importTest

app = Flask(__name__)
app.register_blueprint(importTest, url_prefix="")

@app.route("/")
def test():
    return "<h1>test</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)
