from flask import Flask, render_template
from noticias import Noticia

app = Flask(__name__)

lista_noticia = [
                 Noticia(0, "Por orientação do Comitê Covid", "Por orientação do Comitê Covid, governo volta a obrigar máscara em locais fechados no Acre", "Iryá Rodrigues, g1 AC", "Após anunciar o fim da obrigatoriedade do uso de máscara no Acre em locais abertos ou fechados, o governador Gladson Cameli voltou atrás e decidiu manter a medida preventiva contra a Covid-19. O novo decreto foi publicado na edição desta quarta-feira (16) do Diário Oficial do Estado (DOE). No dia 8 de março, o governo havia informado que, com o fim do último decreto que estabelecia o dia 15 de janeiro deste ano como data limite da recomendação, o uso de máscara não era mais obrigatório no estado. Apesar disso, recomendou o uso da proteção em locais fechados e com aglomeração." , 1),
                 Noticia(1, "noticia 2", "esse é o corpo da noticia 2",
                         "Fulo de tal2", " Corpo extend da noticia", 2),
                 Noticia(2, "noticia 3", "esse é o corpo da noticia 3",
                         "Fulo de tal3", " Corpo extend da noticia", 3),
                 Noticia(3, "noticia 4", "esse é o corpo da noticia 4",
                         "Fulo de tal4", " Corpo extend da noticia", 4),
                 Noticia(4, "noticia 5", "esse é o corpo da noticia 5",
                         "Fulo de tal5", " Corpo extend da noticia", 5),
                 Noticia(5, "noticia 6", "esse é o corpo da noticia 6",
                         "Fulo de tal6", " Corpo extend da noticia", 6),
                 Noticia(6, "noticia 7", "esse é o corpo da noticia 7",
                         "Fulo de tal7", " Corpo extend da noticia", 7),
                 Noticia(7, "noticia 8", "esse é o corpo da noticia 8",
                         "Fulo de tal8", " Corpo extend da noticia", 8),
                 ]


@app.route("/")
def home():
    return render_template("index.html", news1=lista_noticia)

@app.route("/maislidas")
def mais_lidas():
    return render_template("news-2.html")

@app.route("/news/<int:id>")
def news(id):
        for noticia in lista_noticia: 
                if noticia.get_id() == id:
                        return render_template("news.html", noticia=noticia)

@app.route("/nl")
def nl():
    return render_template("newsletter.html", news1=lista_noticia)


if __name__ == "__main__":
    app.run(debug=True)
