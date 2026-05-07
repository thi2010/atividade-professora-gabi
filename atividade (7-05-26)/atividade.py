from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pizzaria/<sabor>')
def pizza(sabor):

    if sabor == "calabresa":
        return render_template("calabresa.html")

    elif sabor == "frango":
        return render_template("frango.html")

    else:
        return "Sabor não disponível"

app.run(debug=True)