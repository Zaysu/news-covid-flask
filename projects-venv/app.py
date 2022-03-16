from flask import Flask, render_template
from noticias import Noticia

app = Flask(__name__)

lista_noticia = [Noticia(0, "noticia 1", "esse é o corpo da noticia 1", "Fulo de tal", 1),
                 Noticia(1, "noticia 2", "esse é o corpo da noticia 2",
                         "Fulo de tal2", 2),
                 Noticia(2, "noticia 3", "esse é o corpo da noticia 3",
                         "Fulo de tal3", 3),
                 Noticia(3, "noticia 4", "esse é o corpo da noticia 4",
                         "Fulo de tal4", 4),
                 Noticia(4, "noticia 5", "esse é o corpo da noticia 5",
                         "Fulo de tal5", 5),
                 Noticia(5, "noticia 6", "esse é o corpo da noticia 6",
                         "Fulo de tal6", 6),
                 Noticia(6, "noticia 7", "esse é o corpo da noticia 7",
                         "Fulo de tal7", 7),
                 Noticia(7, "noticia 8", "esse é o corpo da noticia 8",
                         "Fulo de tal8", 8),

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
