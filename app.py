import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome development team! 11"

@app.route('/covid19')
def hello():
    return 'Please stay home update 5 '

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
