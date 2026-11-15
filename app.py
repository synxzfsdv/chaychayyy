from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# Main page is now the Dashboard
@app.route("/")
def dashboard():
    now = datetime.now()
    # You can pass dummy stats here for now
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


# Your calendar route
@app.route("/calendar")
def calendar_view():
    now = datetime.now()
    return render_template("index.html", year=now.year, month=now.strftime("%B"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Redirect to dashboard upon successful login
        return redirect(url_for("dashboard"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)