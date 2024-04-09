from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status":200, "message": "API Do Luiz_Gustavo_Arduino_Batista"})

@app.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a })

@app.route("/argumentos/<string:nome>")
def argumento(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos")
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})