import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome development team! update 2"

@app.route('/test')
def hello():
    return '<h1>Please stay home </h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
