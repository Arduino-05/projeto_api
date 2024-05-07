from flask import Flask, jsonify, request, Blueprint
from randan_data import data
import funcoes
# app = Flask(__name__)

bp = Blueprint("api", __name__)



@bp.route("/api/", methods= ["GET"])
def index():
    return jsonify({"status":200, "message": "API Do Luiz_Gustavo_Arduino_Batista"})

@bp.route("/api/aleatorios", methods= ["GET"])
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a })

@bp.route("/api/argumentos/<string:nome>", methods= ["GET"])
def argumento(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route("/api/argumentos", methods= ["GET"])
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@bp.route("/api/idades", methods= ["GET"])
def idades():
    num = funcoes.maiores(data)
    return jsonify({"status": 200, "data": num})

@bp.route("/api/salario", methods= ["GET"])
def salario():
    salario = funcoes.salario(data)
    return jsonify({"status": 200,"data": salario})

@bp.route("/api/maior_salario", methods= ["GET"])
def max():
    max = funcoes.maxsalarios(data)
    return jsonify({"status": 200, "data": max})

@bp.route("/api/profissoes", methods= ["GET"])
def profissoes():
    profissoes = funcoes.media_profissao(data)
    return jsonify({"status": 200, "data":profissoes})

@bp.route("/api/idade/<string:tipo>")
def sexos(tipo: str):
    
    sexo = funcoes.sexoidade(data)
    cout = sexo[0]
    coutm = sexo[1]
    inter = sexo[2] , sexo[3]
    
    if tipo == "f":
        return jsonify({"status":200, "data":cout})
    elif tipo == "m":
        return jsonify({"status":200, "data":coutm})
    elif tipo == "intervalo":
        return jsonify({"status":200, "data":inter})

