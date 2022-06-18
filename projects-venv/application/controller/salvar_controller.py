from flask import render_template, request
from application import app
from application.model.entity.comentario import Comentario
from application.model.dao.comentario_dao import lista_comentarios


@app.route('/salvar', methods=['POST', 'GET'])
def salvar():
        nome = request.form.get('nome')
        email = request.form.get('email')
        comentario = request.form.get('comentario')
        dados = Comentario(nome, email, comentario)
        lista_comentarios.append(dados)
        return render_template("newsSalvas.html", comentario=comentario)