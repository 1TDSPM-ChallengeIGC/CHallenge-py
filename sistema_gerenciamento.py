from conexao_db import ConexaoDB
from crud import CRUD

class SistemaGerenciamento:
    def __init__(self):
        self.conexao = ConexaoDB()
        self.crud = CRUD(self.conexao)

    def menu_principal(self):
        while True:
            print("\nMenu Principal:")
            print("1. Inserir cliente")
            print("2. Consultar clientes")
            print("3. Atualizar cliente")
            print("4. Excluir cliente")
            print("5. Exportar dados para JSON")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_cliente()
            elif opcao == "2":
                self.consultar_clientes()
            elif opcao == "3":
                self.atualizar_cliente()
            elif opcao == "4":
                self.excluir_cliente()
            elif opcao == "5":
                self.exportar_clientes_json()
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def inserir_cliente(self):
        print("Cadastro de Cliente")
        nome = self.validar_entrada("Nome: ")
        cpf = self.validar_entrada("CPF: ")
        email = self.validar_entrada("Email: ")
        tel = self.validar_entrada("Telefone: ")
        self.crud.inserir_cliente(nome, cpf, email, tel)

    def consultar_clientes(self):
        clientes = self.crud.consultar_clientes()
        for cliente in clientes:
            print(cliente)

    def atualizar_cliente(self):
        cpf_clie = self.validar_entrada("CPF do cliente a atualizar: ")
        nome = self.validar_entrada("Nome: ")
        email = self.validar_entrada("Email: ")
        tel = self.validar_entrada("Telefone: ")
        self.crud.atualizar_cliente(cpf_clie, nome, email, tel)

    def excluir_cliente(self):
        cpf_clie = self.validar_entrada("CPF do cliente a excluir: ")
        self.crud.excluir_cliente(cpf_clie)

    def exportar_clientes_json(self):
        self.crud.exportar_clientes_json()

    @staticmethod
    def validar_entrada(mensagem):
        return input(mensagem)

    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email