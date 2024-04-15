from flask import Flask, jsonify, request
from randan_data import data
import funcoes

app = Flask(__name__)

@app.route("/", methods=("GET", ))
def index():
    return jsonify({"status":200, "message": "API Do Luiz_Gustavo_Arduino_Batista"})

@app.route("/aleatorios", methods=("GET", ))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a })

@app.route("/argumentos/<string:nome>", methods=("GET", ))
def argumento(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos", methods=("GET", ))
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@app.route("/idades", methods=("GET", ))
def idades():
    num = funcoes.maiores(data)
    return jsonify({"status": 200, "data": num})

@app.route("/salario", methods=("GET", ))
def salario():
    salario = funcoes.salario(data)
    return jsonify({"status": 200,"data": salario})

@app.route("/maior_salario", methods=("GET", ))
def max():
    max = funcoes.maxsalarios(data)
    return jsonify({"status": 200, "data": max})

@app.route("/profissoes", methods=("GET", ))
def profissoes():
    profissoes = funcoes.media_profissao(data)
    return jsonify({"status": 200, "data":profissoes})

@app.route("/idades/sexo=true")
def sexo():
    sexo = funcoes.sexoidade(data)
    return jsonify({"status":200, "data":sexo})