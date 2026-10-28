import sqlite3
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "filmes.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "catalogo-filmes-secret"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                nota REAL NOT NULL
            )
            """
        )
        conn.commit()


init_db()


@app.route("/")
def index():
    conn = get_db_connection()
    filmes = conn.execute("SELECT * FROM filmes ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", filmes=filmes)


@app.route("/novo", methods=["GET", "POST"])
def novo_filme():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        genero = request.form.get("genero", "").strip()
        ano = request.form.get("ano", "")
        nota = request.form.get("nota", "")

        if not titulo or not genero or not ano or not nota:
            flash("Preencha todos os campos.")
            return render_template("form.html", filme=None, action="Cadastrar")

        try:
            ano = int(ano)
            nota = float(nota)
        except ValueError:
            flash("Ano e nota devem ser valores válidos.")
            return render_template("form.html", filme=None, action="Cadastrar")

        if ano < 1900 or ano > 2100:
            flash("O ano deve estar entre 1900 e 2100.")
            return render_template("form.html", filme=None, action="Cadastrar")

        if nota < 1 or nota > 10:
            flash("A nota deve ficar entre 1 e 10.")
            return render_template("form.html", filme=None, action="Cadastrar")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO filmes (titulo, genero, ano, nota) VALUES (?, ?, ?, ?)",
            (titulo, genero, ano, nota),
        )
        conn.commit()
        conn.close()

        flash("Filme cadastrado com sucesso!")
        return redirect(url_for("index"))

    return render_template("form.html", filme=None, action="Cadastrar")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_filme(id):
    conn = get_db_connection()
    filme = conn.execute("SELECT * FROM filmes WHERE id = ?", (id,)).fetchone()

    if filme is None:
        conn.close()
        flash("Filme não encontrado.")
        return redirect(url_for("index"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        genero = request.form.get("genero", "").strip()
        ano = request.form.get("ano", "")
        nota = request.form.get("nota", "")

        if not titulo or not genero or not ano or not nota:
            flash("Preencha todos os campos.")
            conn.close()
            return render_template("form.html", filme=dict(filme), action="Editar")

        try:
            ano = int(ano)
            nota = float(nota)
        except ValueError:
            flash("Ano e nota devem ser valores válidos.")
            conn.close()
            return render_template("form.html", filme=dict(filme), action="Editar")

        if ano < 1900 or ano > 2100:
            flash("O ano deve estar entre 1900 e 2100.")
            conn.close()
            return render_template("form.html", filme=dict(filme), action="Editar")

        if nota < 1 or nota > 10:
            flash("A nota deve ficar entre 1 e 10.")
            conn.close()
            return render_template("form.html", filme=dict(filme), action="Editar")

        conn.execute(
            "UPDATE filmes SET titulo = ?, genero = ?, ano = ?, nota = ? WHERE id = ?",
            (titulo, genero, ano, nota, id),
        )
        conn.commit()
        conn.close()

        flash("Filme atualizado com sucesso!")
        return redirect(url_for("index"))

    conn.close()
    return render_template("form.html", filme=dict(filme), action="Editar")


@app.route("/excluir/<int:id>", methods=["POST"])
def excluir_filme(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM filmes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash("Filme excluído com sucesso!")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
