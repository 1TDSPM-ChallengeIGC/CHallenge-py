print("Inicio do programa")

lista_usuario = []
lista_mecanico = []

def menu():
    return """
--------------------------------
    M E N U - P R I N C I P A L \n
    - (U)suario Cadastrar
    - (M)ecânico Cadastrar
    - (L)istar Usuarios Cadastrados
    - L(I)star Mecanicos Cadastrados
    - (A)tualizar Usuario/Mecanico
    - (E)xcluir Usuario/Mecanico
    - (Q)uem Somos
    - (H)elp
    - (C)hatBot
    - (S)air
--------------------------------
"""

def continuar():
    while True:
        print("Gostaria de voltar ao menu principal? (S/N)")
        voltar_usu = input().upper().strip()
        if voltar_usu == "S":
            return True
        elif voltar_usu == "N":
            print("Até Breve!")
            return False
        else:
            print("Por favor, digite S para (Sim) ou N para (Não)!")

def validar_entrada(prompt, tipo=str):
    while True:
        try:
            valor = tipo(input(prompt).strip())
            if tipo == str and valor == "":
                raise ValueError("A entrada não pode ser vazia.")
            return valor
        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.")

def cadastro_usuario():
    print("Cadastrar Usuario!")
    nome = validar_entrada("Informe seu nome: ")
    email = validar_entrada("Informe o seu email: ")
    placa = validar_entrada("Informe sua placa: ")
    print(f"Parabéns {nome}, você e seu carro {placa} estão cadastrados no nosso sistema!")
    return {"nome": nome, "email": email, "placa": placa}

def cadastro_mecanico():
    print("Cadastrar Mecânico!")
    nome_mec = input("Informe o nome do mecânico: ")
    email_mec = input("Informe o email do mecânico: ")

    while True:
        try:
            salario_mec = float(input("Informe o sálario do mecânico: "))
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o salário.")
    
    print(f"Bem-vindo {nome_mec}, e seu salário mensal será de R$ {salario_mec:.2f}")
    d_mec = {"nome": nome_mec, "email": email_mec, "salario": salario_mec}
    return d_mec

def listar_dados(lista, tipo):
    if lista:
        for idx, item in enumerate(lista):
            print(f"{idx+1} - {item}")
            print("-" * 50)
    else:
        print(f"Nenhum {tipo} cadastrado.")
    input("Aperte <ENTER> para continuar")

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
    input("Aperte <ENTER> para continuar")

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
    input("Aperte <ENTER> para continuar")

def quem_somos():
    print("Quem Somos!")
    print("Somos:\nGuilherme R\nIgor\nCristian\nE iremos mudar o mundo!!")

def help():
    print("Help!")
    pergunta = input("Você está com dificuldades de acessar a página? (S/N) ").upper().strip()
    if pergunta == "S":
        print("Tente atualizar a página ou ligue para nossos serviços humanos, tel: (11) 3687-3779")
    return continuar()

def sair():
    print("Até Breve!")
    return False

def invalido():
    print("Opção Inválida, digite um dos números do Menu.")
    input("Aperte <ENTER> para continuar")

executando = True
while executando:
    print(menu())
    opcao = input("Digite a letra entre () da opcão desejada: ").upper().strip()
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

print("Fim do Programa!")
