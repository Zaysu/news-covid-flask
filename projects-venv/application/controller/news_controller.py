from flask import render_template, request
from application import app
from application.model.dao.noticia_dao import lista_noticia
from application.model.entity.noticias import Noticia
from application.model.dao.comentario_dao import lista_comentarios


@app.route("/news/<int:id>")
def news(id):
    for noticia in lista_noticia:
        if noticia.get_id() == id:
                return render_template("news.html", noticia=noticia, lista_comentarios=lista_comentarios)

        
