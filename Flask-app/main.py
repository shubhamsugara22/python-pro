from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations , its a web app"
