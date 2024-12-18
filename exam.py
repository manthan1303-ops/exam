# create own Docker image for any application developed by using python or php or nodejs or any other plateform and create and run its containor on docker engine.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
