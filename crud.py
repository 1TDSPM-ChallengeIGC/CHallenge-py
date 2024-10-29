# crud.py
import json
import requests  # Certifique-se de ter requests instalado: pip install requests

class CRUD:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_cliente(self, nome, cpf, email, tel):
        query = "INSERT INTO cliente (cpf_clie, nome_clie, email_clie, tel_clie) VALUES (:1, :2, :3, :4)"
        self.conexao.executar_insert_update_delete(query, [cpf, nome, email, tel])
        print("Cliente inserido com sucesso.")

    def consultar_clientes(self):
        query = "SELECT * FROM cliente"
        return self.conexao.executar_query(query)

    def atualizar_cliente(self, cpf_clie, nome=None, email=None, tel=None):
        query = "UPDATE cliente SET nome_clie = :1, email_clie = :2, tel_clie = :3 WHERE cpf_clie = :4"
        self.conexao.executar_insert_update_delete(query, [nome, email, tel, cpf_clie])
        print("Cliente atualizado com sucesso.")

    def excluir_cliente(self, cpf_clie):
        query = "DELETE FROM cliente WHERE cpf_clie = :1"
        self.conexao.executar_insert_update_delete(query, [cpf_clie])
        print("Cliente excluído com sucesso.")

    def exportar_clientes_json(self, file_path="clientes.json"):
        clientes = self.consultar_clientes()
        with open(file_path, 'w') as f:
            json.dump(clientes, f)
        print(f"Dados exportados para {file_path}")
