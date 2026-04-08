from flask import Flask, url_for

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    print(idade)
    print(type(idade))
    print(altura)
    print(type(altura))
    return {
        'nome': usuario,
        'idade': idade,
        'altura': altura,
    }

@app.route("/bemvindo", methods=["GET", "POST"])
def bem_vindo():
    return {
        'message': 'Olá mundo'
    }

#na rota com ("/bemvindo/") vai redirecionar para a pagina correta, sem / no final ai a pagina é unica e se for colocada da erro!

with app.test_request_context():
    print(url_for('hello_world', usuario='pedro', idade=23, altura=1.89))
    print(url_for('bem_vindo', next="/"))