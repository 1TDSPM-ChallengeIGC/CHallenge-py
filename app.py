from flask import Flask, request, jsonify
from sistema_gerenciamento import SistemaGerenciamento

app = Flask(__name__)
sistema = SistemaGerenciamento()

@app.route('/clientes', methods=['POST'])
def inserir_cliente():
    data = request.json
    nome = data.get("nome")
    cpf = data.get("cpf")
    email = data.get("email")
    tel = data.get("telefone")
    sistema.crud.inserir_cliente(nome, cpf, email, tel)
    return jsonify({"message": "Cliente inserido com sucesso"}), 201

@app.route('/clientes', methods=['GET'])
def consultar_clientes():
    clientes = sistema.crud.cons
