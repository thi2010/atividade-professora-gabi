from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = "chave_aleatoria_99"


CREDENCIAIS = {"login": "aluno", "senha": "4321"}


@app.route('/')
def inicio(): 
    return '<h2>Bem-vindo!</h2><a href="/entrar">Fazer Login</a>'


@app.route('/rotalogin')
def rotalogin(): 
    return 'Rota secreta encontrada!<br><a href="/">Voltar</a>'


@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        
        usuario = request.form.get('txt_user')
        pwd = request.form.get('txt_pwd')
        
        if usuario == CREDENCIAIS["login"] and pwd == CREDENCIAIS["senha"]:
            session['corrente'] = usuario
            return redirect('/painel')
        return 'Dados inválidos! <a href="/entrar">Voltar</a>'
    
    return '<form method="POST"><input name="txt_user" placeholder="User"><input type="password" name="txt_pwd" placeholder="Senha"><button>Logar</button></form>'


@app.route('/painel')
def painel():
    if 'corrente' not in session: 
        return redirect('/entrar')
    return f'<h2>Painel do Usuário</h2><p>Ativo: {session["corrente"]}</p><a href="/sair">Sair</a>'


@app.route('/sair')
def sair():
    session.clear()
    return redirect('/entrar')

if __name__ == '__main__':
    app.run(debug=True)