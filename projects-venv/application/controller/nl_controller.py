from flask import render_template
from application import app
from application.model.dao.noticia_dao import lista_noticia

@app.route("/nl")
def nl():
    return render_template("newsletter.html", news1=lista_noticia)