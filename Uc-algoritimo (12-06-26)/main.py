from flask import(Flask, render_template, session, redirect, url_for, request, flash)
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chave-aula-uc31'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route('/')
def inicio():

    nome = session.get('nome', None)
    tema = session.get('tema', 'claro')
    idioma = session.get('idioma', 'pt')
    visitas = session.get('visitas', 0)

    session['visitas'] = visitas + 1

    return render_template(
        'inicio.html',
        nome=nome,
        tema=tema,
        idioma=idioma,
        visitas=session['visitas']
    )
app.route('/personalizar', methods=['GET', 'POST'])
def personalizar():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip().title()
        tema = request.form.get('tema', 'claro')
        idioma = request.form.get('idioma', 'pt')
        lembrar = request.form.get('lembrar')

        if not nome:

            session['nome'] = nome
            session['tema'] = tema
            session['idioma'] = idioma

            if lembrar == 'sim':
                session.permanent = True
            else: