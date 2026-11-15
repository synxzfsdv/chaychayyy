from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.now()
    return render_template("index.html", year=now.year, month=now.strftime("%B"))


# Added login route
@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)