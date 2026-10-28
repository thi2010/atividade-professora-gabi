# Catálogo de Filmes

Sistema web em Flask para cadastrar, listar, editar e excluir filmes utilizando SQLite.

## Como executar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:5000.

## Deploy no Render

1. Crie um repositório no GitHub.
2. Conecte o projeto ao Render.
3. Escolha "New > Web Service".
4. Use a configuração padrão com o arquivo `Procfile`.
5. Faça o deploy.

> O SQLite no Render é temporário e os dados podem ser perdidos após reinicializações do serviço.
