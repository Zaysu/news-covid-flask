from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/hello")
def ola_mundo():
    return "Ola Mundo"

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
