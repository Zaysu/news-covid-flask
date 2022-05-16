from flask import render_template
from application import app
from application.model.dao.noticia_dao import lista_noticia


@app.route("/news/<int:id>")
def news(id):
        for noticia in lista_noticia: 
                if noticia.get_id() == id:
                        return render_template("news.html", noticia=noticia)