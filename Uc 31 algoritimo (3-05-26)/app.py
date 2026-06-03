from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():

    nome = request.form['nome'].strip().title()
    email = request.form['email'].strip().lower()

    if len(nome) < 8:
        return "Nome invalido"

    if "@" not in email:
        return "Email invalido"

    return render_template('resultado.html', nome=nome, email=email)

app.run(debug=True)