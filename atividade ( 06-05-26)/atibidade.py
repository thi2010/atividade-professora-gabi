from flask import Flask

app = Flask(__name__)


@app.route('/ola/<nome>')
def ola(nome):
    return "Olá " + nome + "! Seja bem-vinda ao sistema."


@app.route('/calculo/<int:n1>/<int:n2>')
def calc(n1, n2):
    s = n1 + n2
    return "A soma de " + str(n1) + " + " + str(n2) + " é " + str(s)


@app.route('/idade/<nome>/<int:idade>')
def idade(nome, idade):
    if idade >= 18:
        return nome + " é maior de idade."
    else:
        return nome + " é menor de idade."


@app.route('/produto/<nome>/<float:preco>')
def prod(nome, preco):
    return "O produto " + nome + " custa R$ " + str(preco)


@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    res = ""
    for i in range(vezes):
        res = res + palavra + " "
    return res

app.run()