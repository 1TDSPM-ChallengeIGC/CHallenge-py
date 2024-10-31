import json
import requests
from crud import CRUD

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
            print("5. Exportar Clientes")
            print("6. Consultar Usuários da API Externa")
            print("7. Sair")

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
                self.exportar_clientes()
            elif opcao == "6":
                self.consultar_usuarios_api()
            elif opcao == "7":
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
        print("\nVamos cadastrar um novo cliente! 📝")
        nome = self.validar_entrada("Nome: ", self.crud.validar_nome)
        cpf = self.validar_entrada("CPF: ", self.crud.validar_cpf)
        email = self.validar_entrada("Email: ", self.crud.validar_email)
        tel = self.validar_entrada("Telefone: ", self.crud.validar_telefone)

        self.crud.inserir_cliente(nome, cpf, email, tel)
        print("Cliente cadastrado com sucesso! 🎉")

    def consultar_clientes(self):
        print("\nComo você deseja consultar os clientes? 🤔")
        print("1. Por CPF")
        print("2. Por Nome")
        print("3. Listar Todos")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            cpf = self.validar_entrada("Digite o CPF: ", self.crud.validar_cpf)
            clientes = self.crud.consultar_clientes(cpf=cpf)
        elif opcao == "2":
            nome = input("Digite o nome: ")
            clientes = self.crud.consultar_clientes(nome=nome)
        else:
            clientes = self.crud.consultar_clientes()

        if clientes:
            print("\nClientes encontrados: 📋")
            print("=" * 40)  
            for cliente in clientes:
                print(f"Nome: {cliente['nome']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"Email: {cliente['email']}")
                print(f"Telefone: {cliente['telefone']}")
                print("-" * 40)  
            print("=" * 40)  
        else:
            print("Nenhum cliente encontrado com os critérios informados. 😞")

    def atualizar_cliente(self):
        print("\nVamos atualizar os dados de um cliente! 🔄")
        cpf_clie = self.validar_entrada("CPF do cliente a atualizar: ", self.crud.validar_cpf)
        nome = input("Novo Nome (pressione Enter para manter): ")
        email = input("Novo Email (pressione Enter para manter): ")
        tel = input("Novo Telefone (pressione Enter para manter): ")

        self.crud.atualizar_cliente(cpf_clie, nome or None, email or None, tel or None)
        print("Cliente atualizado com sucesso! ✅")

    def excluir_cliente(self):
        print("\nVamos excluir um cliente! 🚮")
        print("Como você deseja excluir o cliente?")
        print("1. Por CPF")
        print("2. Por Nome")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            cpf_clie = self.validar_entrada("Digite o CPF do cliente a excluir: ", self.crud.validar_cpf)
            self.crud.excluir_cliente(cpf_clie)
            print("Cliente excluído com sucesso! ❌")
        elif opcao == "2":
            nome_clie = input("Digite o Nome do cliente a excluir: ")
            clientes = self.crud.consultar_clientes(nome=nome_clie)
            if clientes:
                for cliente in clientes:
                    confirmacao = input(f"Tem certeza que deseja excluir o cliente {cliente['nome']} (CPF: {cliente['cpf']})? (s/n) ")
                    if confirmacao.lower() == 's':
                        self.crud.excluir_cliente(cliente['cpf'])
                        print("Cliente excluído com sucesso! ❌")
            else:
                print("Nenhum cliente encontrado com o nome informado. 😞")
        else:
            print("Opção inválida. Por favor, escolha novamente.")

    def exportar_clientes(self):
        print("\nComo você deseja exportar os clientes? 📤")
        print("1. Exportar todos os clientes")
        print("2. Exportar um cliente específico pelo nome")
        print("3. Exportar todos os clientes cujo nome ou sobrenome começam com uma letra específica")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            clientes = self.crud.consultar_clientes()
            self.salvar_json(clientes, "todos_clientes.json")
            print("Todos os clientes foram exportados com sucesso! 📁")
        elif opcao == "2":
            nome = input("Digite o nome do cliente a exportar: ")
            clientes = self.crud.consultar_clientes(nome=nome)
            if clientes:
                self.salvar_json(clientes, f"cliente_{nome}.json")
                print(f"O cliente {nome} foi exportado com sucesso! 📁")
            else:
                print("Nenhum cliente encontrado com o nome informado. 😞")
        elif opcao == "3":
            letra = input("Digite a letra: ")
            clientes = self.crud.consultar_clientes(nome=letra)
            if clientes:
                self.salvar_json(clientes, f"clientes_com_letra_{letra}.json")
                print(f"Clientes com nomes que começam com a letra '{letra}' foram exportados com sucesso! 📁")
            else:
                print("Nenhum cliente encontrado com a letra informada. 😞")
        else:
            print("Opção inválida. Por favor, escolha novamente.")

    def consultar_usuarios_api(self):
        print("\nConsultando usuários da API externa... 🌐")
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)

        if response.status_code == 200:
            usuarios = response.json()
            print("\nUsuários encontrados na API:")
            for usuario in usuarios:
                print(f"Nome: {usuario['name']}")
                print(f"Email: {usuario['email']}")
                print(f"Telefone: {usuario['phone']}")
                print("-" * 40)
        else:
            print("Erro ao acessar a API. Status code:", response.status_code)

    def salvar_json(self, dados, nome_arquivo):
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
