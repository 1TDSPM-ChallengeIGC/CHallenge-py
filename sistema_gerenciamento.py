from crud import CRUD
from conexao_db import ConexaoDB

class SistemaGerenciamento:
    def __init__(self, conexao):
        self.conexao = conexao
        self.crud = CRUD(conexao)

    def menu_principal(self):
        while True:
            print("\nMenu Principal")
            print("1. Inserir Cliente")
            print("2. Consultar Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
            print("5. Sair")

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
                self.conexao.close()
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

    def validar_entrada(self, prompt, validacao_funcao):
        while True:
            entrada = input(prompt)
            try:
                if validacao_funcao(entrada):
                    return entrada
            except ValueError as e:
                print(e)  
                print("Por favor, tente novamente.")  

    def inserir_cliente(self):
        nome = self.validar_entrada("Nome: ", self.crud.validar_nome)
        cpf = self.validar_entrada("CPF: ", self.crud.validar_cpf)
        email = self.validar_entrada("Email: ", self.crud.validar_email)
        tel = self.validar_entrada("Telefone: ", self.crud.validar_telefone)

        self.crud.inserir_cliente(nome, cpf, email, tel)

    def consultar_clientes(self):
        clientes = self.crud.consultar_clientes()
        for cliente in clientes:
            print(cliente)

    def atualizar_cliente(self):
        cpf_clie = self.validar_entrada("CPF do cliente a atualizar: ", self.crud.validar_cpf)
        nome = self.validar_entrada("Novo Nome (pressione Enter para manter): ", self.crud.validar_nome)
        email = self.validar_entrada("Novo Email (pressione Enter para manter): ", self.crud.validar_email)
        tel = self.validar_entrada("Novo Telefone (pressione Enter para manter): ", self.crud.validar_telefone)

        self.crud.atualizar_cliente(cpf_clie, nome, email, tel)

    def excluir_cliente(self):
        cpf_clie = self.validar_entrada("CPF do cliente a excluir: ", self.crud.validar_cpf)
        self.crud.excluir_cliente(cpf_clie)
