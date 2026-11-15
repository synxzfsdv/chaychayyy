from datetime import datetime
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)
app.secret_key = "super_secret_calendar_key"


@app.route("/")
def dashboard():
    # Send unauthenticated users to login first
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    now = datetime.now()
    stats = {
        "total_tasks": 12,
        "completed_tasks": 5,
        "pending_tasks": 7,
    }
    return render_template(
        "dashboard.html",
        year=now.year,
        month=now.strftime("%B"),
        stats=stats,
    )


@app.route("/calendar")
def calendar_view():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    now = datetime.now()
    return render_template("index.html", year=now.year, month=now.strftime("%B"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["logged_in"] = True
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        session["logged_in"] = True
        return redirect(url_for("dashboard"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)