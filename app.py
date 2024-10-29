# app.py
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
    clientes = sistema.crud.consultar_clientes()
    return jsonify(clientes)

@app.route('/clientes/<string:cpf>', methods=['PUT'])
def atualizar_cliente(cpf):
    data = request.json
    nome = data.get("nome")
    email = data.get("email")
    tel = data.get("telefone")
    sistema.crud.atualizar_cliente(cpf, nome, email, tel)
    return jsonify({"message": "Cliente atualizado com sucesso"})

@app.route('/clientes/<string:cpf>', methods=['DELETE'])
def excluir_cliente(cpf):
    sistema.crud.excluir_cliente(cpf)
    return jsonify({"message": "Cliente excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
