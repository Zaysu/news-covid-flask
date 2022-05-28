from flask import render_template
from application import app

@app.route("/nl")
def nl():
    return render_template("newsletter.html")