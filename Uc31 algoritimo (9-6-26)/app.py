from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = request.cookies.get("nome")
    tema = request.cookies.get("tema", "claro")
    return render_template("inicio.html", nome=nome, tema=tema)

@app.route("/salvar", methods=["POST"])
def salvar():
    resp = make_response(redirect("/"))
    resp.set_cookie("nome", request.form["nome"])
    return resp

@app.route("/tema/<t>")
def tema(t):
    resp = make_response(redirect("/"))
    resp.set_cookie("tema", t)
    return resp

app.run(debug=True)