from flask import Flask
from flask import render_template

__author__ = "cGm"

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
