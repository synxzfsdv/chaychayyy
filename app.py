from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.now()
    return render_template("index.html", year=now.year, month=now.strftime("%B"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Here you can later check username/password.
        # For now, it logs them in and redirects to the calendar page:
        return redirect(url_for("index"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)