from flask import Flask

app = Flask(__name__)

@app.route('/filme/<g>')
def filme(g):

    if g == "acao":
        return "Filme de ação"

    elif g == "comedia":
        return "Filme de comédia"

    else:
        return "Gênero não disponível"

app.run()