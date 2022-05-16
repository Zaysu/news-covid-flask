from flask import render_template
from application import app

@app.route("/maislidas")
def mais_lidas():
    return render_template("news-2.html")