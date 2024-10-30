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
        # Verifica se existem registros relacionados na tabela 'guincho' ou 'carro'
        if self.verificar_registros_relacionados(cpf_clie):
            print("Não é possível excluir o cliente. Existem registros relacionados nas tabelas 'guincho' ou 'carro'.")
            return

        query = "DELETE FROM cliente WHERE cpf_clie = :1"
        self.conexao.executar_insert_update_delete(query, [cpf_clie])
        print("Cliente excluído com sucesso.")

    def verificar_registros_relacionados(self, cpf_clie):
        # Verifique o nome correto da coluna nas tabelas 'guincho' e 'carro'
        query_guincho = "SELECT COUNT(*) FROM guincho WHERE cpf_clie = :1"
        resultado_guincho = self.conexao.executar_query(query_guincho, [cpf_clie])

        query_carro = "SELECT COUNT(*) FROM carro WHERE cpf_clie = :1"
        resultado_carro = self.conexao.executar_query(query_carro, [cpf_clie])

        # Retorna True se houver registros relacionados em qualquer uma das tabelas
        return resultado_guincho[0][0] > 0 or resultado_carro[0][0] > 0

    def exportar_clientes_json(self, file_path="clientes.json"):
        clientes = self.consultar_clientes()
        with open(file_path, 'w') as f:
            json.dump(clientes, f)
        print(f"Dados exportados para {file_path}")
