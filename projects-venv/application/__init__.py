from flask import Flask
import os

app = Flask(__name__,
        static_folder=os.path.abspath("application/view/static"),
        template_folder=os.path.abspath("application/view/templates"))
            
from application.controller import home_controller
from application.controller import maislidas_controller
from application.controller import news_controller
from application.controller import nl_controller
from application.controller import salvar_controller
from application.controller import cad_coment_controller

if __name__ == "__main__":
    app.run(debug=True)