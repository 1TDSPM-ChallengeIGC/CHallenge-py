import re
import json

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
        # Verifica se existem registros relacionados na tabela 'guincho'
        if self.verificar_registros_relacionados(cpf_clie):
            print("Não é possível excluir o cliente. Existem registros relacionados na tabela 'guincho'.")
            return

        query = "DELETE FROM cliente WHERE cpf_clie = :1"
        self.conexao.executar_insert_update_delete(query, [cpf_clie])
        print("Cliente excluído com sucesso.")

    def verificar_registros_relacionados(self, cpf_clie):
        query = "SELECT COUNT(*) FROM guincho WHERE cpf_clie = :1"
        resultado = self.conexao.executar_query(query, [cpf_clie])
        return resultado[0][0] > 0  # Retorna True se houver registros relacionados

    def exportar_clientes_json(self, file_path="clientes.json"):
        clientes = self.consultar_clientes()
        with open(file_path, 'w') as f:
            json.dump(clientes, f)
        print(f"Dados exportados para {file_path}")

    def validar_nome(self, nome):
        if not nome or len(nome) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres. Por favor, insira um nome válido.")
        return True

    def validar_cpf(self, cpf):
        if not re.match(r'^\d{11}$', cpf):
            raise ValueError("O CPF deve ter 11 dígitos numéricos. Por favor, insira um CPF válido.")
        return True

    def validar_email(self, email):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("O e-mail inserido não é válido. Por favor, insira um e-mail válido.")
        return True

    def validar_telefone(self, telefone):
        if not re.match(r'^\d{10,11}$', telefone):
            raise ValueError("O telefone deve ter 10 ou 11 dígitos numéricos. Por favor, insira um telefone válido.")
        return True
