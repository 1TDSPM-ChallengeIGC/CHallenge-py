import re

print("Bem-vindo ao sistema de gerenciamento de usuários e mecânicos!")

lista_usuario = []
lista_mecanico = []

def menu():
    return """
--------------------------------
       M E N U - P R I N C I P A L 
--------------------------------
    - (U)suario Cadastrar
    - (M)ecânico Cadastrar
    - (L)istar Usuarios Cadastrados
    - L(I)star Mecanicos Cadastrados
    - (A)tualizar Usuario/Mecanico
    - (E)xcluir Usuario/Mecanico
    - (Q)uem Somos
    - (H)elp
    - (S)air
--------------------------------
"""

def continuar():
    while True:
        voltar_usu = input("Deseja voltar ao menu principal? (S/N): ").upper().strip()
        if voltar_usu == "S":
            return True
        elif voltar_usu == "N":
            print("Saindo do sistema. Até breve!")
            return False
        else:
            print("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")

def validar_entrada(prompt, tipo=str):
    while True:
        try:
            valor = tipo(input(prompt).strip())
            if tipo == str and valor == "":
                raise ValueError("O campo não pode ser vazio.")
            return valor
        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.")

def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao, email):
        return True
    print("Email inválido! Formato esperado: exemplo@dominio.com")
    return False

def validar_placa(placa):
    padrao_antigo = r'^[A-Z]{3}[0-9]{4}$'  
    padrao_novo = r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'  
    if re.match(padrao_antigo, placa) or re.match(padrao_novo, placa):
        return True
    print("Placa inválida! Formato esperado: AAA1234 ou AAA1A23")
    return False

def cadastro_usuario():
    print("Cadastro de Usuário")
    nome = validar_entrada("Nome: ")

    email = validar_entrada("Email: ")
    while not validar_email(email):
        email = validar_entrada("Informe um email válido: ")

    placa = validar_entrada("Placa do carro: ")
    while not validar_placa(placa):
        placa = validar_entrada("Informe uma placa válida: ")

    print(f"Usuário {nome} e seu carro {placa} cadastrados com sucesso!")
    return {"nome": nome, "email": email, "placa": placa}

def cadastro_mecanico():
    print("Cadastro de Mecânico")
    nome_mec = validar_entrada("Nome do mecânico: ")

    email_mec = validar_entrada("Email: ")
    while not validar_email(email_mec):
        email_mec = validar_entrada("Informe um email válido para o mecânico: ")

    salario_mec = 0
    while True:
        try:
            salario_mec = float(validar_entrada("Salário do mecânico (R$): ", float))
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o salário.")

    print(f"Mecânico {nome_mec} cadastrado com salário de R$ {salario_mec:.2f}")
    return {"nome": nome_mec, "email": email_mec, "salario": salario_mec}

def listar_dados(lista, tipo):
    if lista:
        for idx, item in enumerate(lista):
            print(f"{idx+1} - {item}")
        print("-" * 50)
    else:
        print(f"Nenhum {tipo} cadastrado.")
    input("Pressione <ENTER> para continuar")

def atualizar_dados(lista, tipo):
    listar_dados(lista, tipo)
    if lista:
        try:
            indice = int(validar_entrada(f"Informe o número do {tipo} que deseja atualizar: ", int)) - 1
            if 0 <= indice < len(lista):
                if tipo == "usuário":
                    lista[indice] = cadastro_usuario()
                else:
                    lista[indice] = cadastro_mecanico()
                print(f"{tipo.capitalize()} atualizado com sucesso!")
            else:
                print(f"{tipo.capitalize()} não encontrado.")
        except ValueError:
            print("Erro! Informe um número válido.")
    else:
        print(f"Nenhum {tipo} cadastrado.")
    input("Pressione <ENTER> para continuar")

def excluir_dados(lista, tipo):
    listar_dados(lista, tipo)
    if lista:
        try:
            indice = int(validar_entrada(f"Informe o número do {tipo} que deseja excluir: ", int)) - 1
            if 0 <= indice < len(lista):
                excluido = lista.pop(indice)
                print(f"{tipo.capitalize()} {excluido['nome']} excluído com sucesso!")
            else:
                print(f"{tipo.capitalize()} não encontrado.")
        except ValueError:
            print("Erro! Informe um número válido.")
    else:
        print(f"Nenhum {tipo} cadastrado.")
    input("Pressione <ENTER> para continuar")

def quem_somos():
    print("""
    Somos uma equipe dedicada:
    - Guilherme R
    - Igor
    - Cristian
    Juntos, estamos prontos para enfrentar qualquer desafio e oferecer as melhores soluções!
    """)

def help():
    print("Se precisar de ajuda, entre em contato com nosso suporte pelo telefone: (11) 3687-3779.")
    return continuar()

def sair():
    print("Saindo do sistema. Obrigado por usar nosso software!")
    return False

def invalido():
    print("Opção Inválida! Escolha uma opção válida do menu.")
    input("Pressione <ENTER> para continuar")

# Execução principal
executando = True
while executando:
    print(menu())
    opcao = input("Escolha uma opção: ").upper().strip()
    
    if opcao == "U":
        lista_usuario.append(cadastro_usuario())
        executando = continuar()
    elif opcao == "M":
        lista_mecanico.append(cadastro_mecanico())
        executando = continuar()
    elif opcao == "L":
        listar_dados(lista_usuario, "usuário")
    elif opcao == "I":
        listar_dados(lista_mecanico, "mecânico")
    elif opcao == "A":
        sub_opcao = input("Deseja atualizar (U)suario ou (M)ecânico? ").upper().strip()
        if sub_opcao == "U":
            atualizar_dados(lista_usuario, "usuário")
        elif sub_opcao == "M":
            atualizar_dados(lista_mecanico, "mecânico")
        else:
            invalido()
        executando = continuar()
    elif opcao == "E":
        sub_opcao = input("Deseja excluir (U)suario ou (M)ecânico? ").upper().strip()
        if sub_opcao == "U":
            excluir_dados(lista_usuario, "usuário")
        elif sub_opcao == "M":
            excluir_dados(lista_mecanico, "mecânico")
        else:
            invalido()
        executando = continuar()
    elif opcao == "Q":
        quem_somos()
        executando = continuar()
    elif opcao == "H":
        executando = help()
    elif opcao == "S":
        executando = sair()
    else:
        invalido()

print("Programa encerrado.")
