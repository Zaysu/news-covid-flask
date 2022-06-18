from flask import render_template
from application import app
from application.model.dao.comentario_dao import lista_comentarios


@app.route('/comentariossalvos')
def coments():
        return render_template("newsSalvas.html", lista_comentarios=lista_comentarios)