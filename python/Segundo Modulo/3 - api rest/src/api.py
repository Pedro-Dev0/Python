from flask import Flask, url_for

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    print(idade)
    print(type(idade))
    print(altura)
    print(type(altura))
    return f"<p>Hello World! {usuario.upper()}, idade:{idade}</p>"

@app.route("/bemvindo")
def bem_vindo():
    return "<p>Bem vindo!</p>"

#na rota com ("/bemvindo/") vai redirecionar para a pagina correta, sem / no final ai a pagina é unica e se for colocada da erro!

with app.test_request_context():
    print(url_for('olamundo'))
    print(url_for('bemvindo'))