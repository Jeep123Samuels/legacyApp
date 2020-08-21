from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Many Ways To Solve a Problem</h1>"


@app.route("/melisa/samuels/")
def love_view_2():
    return "bly jy is myne my lief... mwah. JP"


@app.route("/melisa/stuur/soen/vir/jp")
def love_view_3():
    return "Mwah op jou bek vrou lief"


@app.route("/jp/maak/ogies/vir/melisa/")
def love_view_4():
    return "Ek gaan jou stoot vanaand... mwah"
