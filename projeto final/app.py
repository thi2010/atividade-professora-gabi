import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "medtech-chave-local")

DATABASE = os.path.join(os.path.dirname(__file__), "medtech.db")


def conectar():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db


def inicializar_banco():
    with conectar() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT,
                data_nascimento TEXT
            );

            CREATE TABLE IF NOT EXISTS consultas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                data_consulta TEXT NOT NULL,
                horario TEXT NOT NULL,
                especialidade TEXT NOT NULL,
                observacoes TEXT,
                status TEXT DEFAULT 'Agendada',
                FOREIGN KEY (paciente_id)
                REFERENCES pacientes(id) ON DELETE CASCADE
            );
        """)


def buscar_pacientes(termo=""):
    with conectar() as db:
        return db.execute("""
            SELECT * FROM pacientes
            WHERE nome LIKE ?
            ORDER BY nome COLLATE NOCASE ASC
        """, (f"%{termo}%",)).fetchall()


def obter_consultas():
    with conectar() as db:
        return db.execute("""
            SELECT consultas.*, pacientes.nome AS paciente_nome
            FROM consultas
            INNER JOIN pacientes
            ON consultas.paciente_id = pacientes.id
            ORDER BY consultas.data_consulta, consultas.horario
        """).fetchall()


@app.route("/")
def inicio():
    termo = request.args.get("q", "")
    pacientes = buscar_pacientes(termo)
    consultas = obter_consultas()

    return render_template(
        "index.html",
        pacientes=pacientes,
        consultas=consultas,
        termo=termo
    )


@app.route("/pacientes/novo", methods=["GET", "POST"])
def novo_paciente():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        telefone = request.form.get("telefone", "").strip()
        email = request.form.get("email", "").strip()
        nascimento = request.form.get("data_nascimento", "")

        if not nome or not telefone:
            flash("Preencha nome e telefone.", "erro")
            return render_template("paciente_form.html", paciente=None)

        with conectar() as db:
            db.execute("""
                INSERT INTO pacientes
                (nome, telefone, email, data_nascimento)
                VALUES (?, ?, ?, ?)
            """, (nome, telefone, email, nascimento))

        flash("Paciente cadastrado com sucesso!", "sucesso")
        return redirect(url_for("inicio"))

    return render_template("paciente_form.html", paciente=None)


@app.route("/pacientes/<int:id>/editar", methods=["GET", "POST"])
def editar_paciente(id):
    with conectar() as db:
        paciente = db.execute(
            "SELECT * FROM pacientes WHERE id = ?", (id,)
        ).fetchone()

        if paciente is None:
            abort(404)

        if request.method == "POST":
            nome = request.form.get("nome", "").strip()
            telefone = request.form.get("telefone", "").strip()
            email = request.form.get("email", "").strip()
            nascimento = request.form.get("data_nascimento", "")

            if not nome or not telefone:
                flash("Nome e telefone são obrigatórios.", "erro")
                return render_template(
                    "paciente_form.html", paciente=paciente
                )

            db.execute("""
                UPDATE pacientes
                SET nome=?, telefone=?, email=?, data_nascimento=?
                WHERE id=?
            """, (nome, telefone, email, nascimento, id))

            flash("Paciente atualizado!", "sucesso")
            return redirect(url_for("inicio"))

    return render_template("paciente_form.html", paciente=paciente)


@app.route("/pacientes/<int:id>/excluir", methods=["POST"])
def excluir_paciente(id):
    with conectar() as db:
        db.execute("DELETE FROM pacientes WHERE id=?", (id,))

    flash("Paciente excluído!", "sucesso")
    return redirect(url_for("inicio"))


@app.route("/consultas/nova", methods=["GET", "POST"])
def nova_consulta():
    pacientes = buscar_pacientes()

    if request.method == "POST":
        paciente_id = request.form.get("paciente_id", type=int)
        data = request.form.get("data_consulta", "")
        horario = request.form.get("horario", "")
        especialidade = request.form.get("especialidade", "")
        observacoes = request.form.get("observacoes", "")

        if not paciente_id or not data or not horario or not especialidade:
            flash("Preencha todos os campos obrigatórios.", "erro")
            return render_template(
                "consulta_form.html", pacientes=pacientes
            )

        if not any(p["id"] == paciente_id for p in pacientes):
            abort(400)

        try:
            datetime.strptime(data, "%Y-%m-%d")
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            flash("Data ou horário inválido.", "erro")
            return render_template(
                "consulta_form.html", pacientes=pacientes
            )

        with conectar() as db:
            db.execute("""
                INSERT INTO consultas
                (paciente_id, data_consulta, horario,
                 especialidade, observacoes)
                VALUES (?, ?, ?, ?, ?)
            """, (
                paciente_id, data, horario,
                especialidade, observacoes
            ))

        flash("Consulta agendada!", "sucesso")
        return redirect(url_for("inicio"))

    return render_template("consulta_form.html", pacientes=pacientes)


@app.route("/consultas/<int:id>/status", methods=["POST"])
def alterar_status(id):
    status = request.form.get("status")

    if status not in ["Agendada", "Concluída", "Cancelada"]:
        abort(400)

    with conectar() as db:
        db.execute(
            "UPDATE consultas SET status=? WHERE id=?",
            (status, id)
        )

    flash("Status atualizado!", "sucesso")
    return redirect(url_for("inicio"))


@app.route("/consultas/<int:id>/excluir", methods=["POST"])
def excluir_consulta(id):
    with conectar() as db:
        db.execute("DELETE FROM consultas WHERE id=?", (id,))

    flash("Consulta excluída!", "sucesso")
    return redirect(url_for("inicio"))


@app.route("/api/pacientes")
def api_pacientes():
    pacientes = buscar_pacientes(request.args.get("q", ""))

    return jsonify([
        {
            "id": p["id"],
            "nome": p["nome"],
            "telefone": p["telefone"],
            "email": p["email"]
        }
        for p in pacientes
    ])


@app.route("/api/consultas")
def api_consultas():
    consultas = obter_consultas()

    return jsonify([
        {
            "id": c["id"],
            "paciente": c["paciente_nome"],
            "data": c["data_consulta"],
            "horario": c["horario"],
            "especialidade": c["especialidade"],
            "status": c["status"]
        }
        for c in consultas
    ])


inicializar_banco()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
from flask import Flask, render_template