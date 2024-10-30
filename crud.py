from conexao_db import ConexaoDB
import json

class CRUD:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_cliente(self, nome, cpf, email, tel):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO cliente (nome, cpf, email, tel)
                    VALUES (:nome, :cpf, :email, :tel)
                """, {'nome': nome, 'cpf': cpf, 'email': email, 'tel': tel})
                self.conexao.commit()
                print("Cliente inserido com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")

    def consultar_clientes(self):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM cliente")
                return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao consultar clientes: {e}")
            return []

    def atualizar_cliente(self, cpf_clie, nome, email, tel):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("""
                    UPDATE cliente
                    SET nome = :nome, email = :email, tel = :tel
                    WHERE cpf = :cpf
                """, {'nome': nome, 'email': email, 'tel': tel, 'cpf': cpf_clie})
                self.conexao.commit()
                print("Cliente atualizado com sucesso.")
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")

    def excluir_cliente(self, cpf_clie):
        try:
            # Verifica se existem carros ou guinchos associados ao cliente
            if self.cliente_tem_carros(cpf_clie):
                self.excluir_carros(cpf_clie)
            if self.cliente_tem_guinchos(cpf_clie):
                self.excluir_guinchos(cpf_clie)

            with self.conexao.cursor() as cursor:
                cursor.execute("DELETE FROM cliente WHERE cpf = :cpf", {'cpf': cpf_clie})
                self.conexao.commit()
                print("Cliente excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")

    def exportar_clientes_json(self):
        clientes = self.consultar_clientes()
        with open('clientes.json', 'w') as arquivo_json:
            json.dump(clientes, arquivo_json, default=str)
            print("Dados dos clientes exportados para clientes.json.")

    def cliente_tem_carros(self, cpf_clie):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM carro WHERE cpf_clie = :cpf", {'cpf': cpf_clie})
                return cursor.fetchone()[0] > 0
        except Exception as e:
            print(f"Erro ao verificar carros do cliente: {e}")
            return False

    def cliente_tem_guinchos(self, cpf_clie):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM guincho WHERE cpf_clie = :cpf", {'cpf': cpf_clie})
                return cursor.fetchone()[0] > 0
        except Exception as e:
            print(f"Erro ao verificar guinchos do cliente: {e}")
            return False

    def excluir_carros(self, cpf_clie):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("DELETE FROM carro WHERE cpf_clie = :cpf", {'cpf': cpf_clie})
                self.conexao.commit()
                print("Carros do cliente excluídos com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir carros do cliente: {e}")

    def excluir_guinchos(self, cpf_clie):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("DELETE FROM guincho WHERE cpf_clie = :cpf", {'cpf': cpf_clie})
                self.conexao.commit()
                print("Guinchos do cliente excluídos com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir guinchos do cliente: {e}")
