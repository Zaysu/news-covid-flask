from flask import render_template
from application import app
from application.model.dao.noticia_dao import lista_noticia


@app.route("/")
def home():
    return render_template("index.html", news1=lista_noticia)