from flask import Flask, url_for

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    print(idade)
    print(type(idade))
    print(altura)
    print(type(altura))
    return f"<p>Hello World! {usuario.upper()}, idade:{idade}</p>"

@app.route("/bemvindo", methods=["GET", "POST"])
def bem_vindo():
    if request.method == "GET":
        return 'É get'
    else:
        return 'We Post'


#na rota com ("/bemvindo/") vai redirecionar para a pagina correta, sem / no final ai a pagina é unica e se for colocada da erro!

with app.test_request_context():
    print(url_for('hello_world', usuario='pedro', idade=23, altura=1.89))
    print(url_for('bem_vindo'))