from flask import Flask, render_template
from noticias import Noticia

app = Flask(__name__)

lista_noticia = [
                 Noticia(0, "Por orientação do Comitê Covid", "Por orientação do Comitê Covid, governo volta a obrigar máscara em locais fechados no Acre", "Iryá Rodrigues, g1 AC", "Após anunciar o fim da obrigatoriedade do uso de máscara no Acre em locais abertos ou fechados, o governador Gladson Cameli voltou atrás e decidiu manter a medida preventiva contra a Covid-19. O novo decreto foi publicado na edição desta quarta-feira (16) do Diário Oficial do Estado (DOE). No dia 8 de março, o governo havia informado que, com o fim do último decreto que estabelecia o dia 15 de janeiro deste ano como data limite da recomendação, o uso de máscara não era mais obrigatório no estado. Apesar disso, recomendou o uso da proteção em locais fechados e com aglomeração." , 1, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(1, "Alagoas registra mais 549 Casos de SarsCOV-2", "Aumento de casos chama atenção diante da média dos últimos cinco dias, quando o registro diário não passou de 100 confirmações",
                         "g1 AL", " Alagoas registrou 549 novos casos de Covid segundo o boletim epidemiológico da Secretaria de Estado da Saúde (Sesau), desta quarta-feira (16). Um aumento expressivo, levando-se em consideração os últimos cinco dias, quando o total de casos no estado não passou de 100 por dia:", 2, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(2, "Amapá registra 4 novos casos", "Boletim epidemiológico desta quarta-feira (16) descreve 14 internados pela doença, sendo 6 na UTI.",
                         "g1 AP", " O Amapá contabilizou 4 casos conhecidos e não registrou mortes por Covid-19 nas últimas 24 horas. Todos os pacientes novos eram de Macapá. Os dados constam no boletim epidemiológico do governo desta quarta-feira (16). Com isso, o estado registra 160.221 casos confirmados e 2.119 óbitos. Os recuperados somam 128.523 pessoas (80,21%). Especialistas acreditam que há muitos que não fazem o exame, que isto continua bastante necessário, assim como o isolamento. Esses fatores podem ocultar muitos casos confirmados de Covid-19 que deixam de entrar nas estatísticas oficiais.", 3, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(3, "noticia 4", "esse é o corpo da noticia 4",
                         "Fulo de tal4", " Corpo extend da noticia", 4, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(4, "noticia 5", "esse é o corpo da noticia 5",
                         "Fulo de tal5", " Corpo extend da noticia", 5, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(5, "noticia 6", "esse é o corpo da noticia 6",
                         "Fulo de tal6", " Corpo extend da noticia", 6, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(6, "noticia 7", "esse é o corpo da noticia 7",
                         "Fulo de tal7", " Corpo extend da noticia", 7, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
                 Noticia(7, "noticia 8", "esse é o corpo da noticia 8",
                         "Fulo de tal8", " Corpo extend da noticia", 8, "https://ichef.bbci.co.uk/news/1024/branded_portuguese/34FA/production/_111226531_corona.jpg"),
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
