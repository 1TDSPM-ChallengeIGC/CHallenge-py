print("Inicio do programa")

# Listas para armazenar os dados
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
    nome_mec = validar_entrada("Informe o nome do mecânico: ")
    email_mec = validar_entrada("Informe o email do mecânico: ")
    salario_mec = validar_entrada("Informe o sálario do mecânico: ", float)
    print(f"Bem-vindo {nome_mec}, e seu salário mensal será de R$ {salario_mec:.2f}")
    return {"nome": nome_mec, "email": email_mec, "salario": salario_mec}

def listar_dados(lista, tipo):
    if lista:
        for item in lista:
            print(item)
            print("-" * 50)
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

def menu_chat():
    return """
--------------------------------
 M E N U - D E - P R O B L E M A S \n
 - (S)uperaquecimento
 - Pane (E)létrica
 - (B)ateria
 - (F)alta de Combustível
 - Carro (T)repidando
 - (P)neus Furados
 - Correia (D)entada
 - Problemas no (C)âmbio
 - (V)oltar
--------------------------------
"""

def continuar_problemas():
    while True:
        voltar = input("Gostaria de voltar ao menu de problemas? (S/N) ").upper().strip()
        if voltar == "S":
            return True
        elif voltar == "N":
            return False
        else:
            print("Por favor, digite S para (Sim) ou N para (Não)!")

def p_superaquecimento():
    print("Se o carro estiver superaquecendo, pare imediatamente, desligue o motor e deixe esfriar.")
    print("Verifique o nível do líquido de arrefecimento e procure por vazamentos.")
    return continuar_problemas()

def p_eletrico():
    print("Em caso de pane elétrica no carro, verifique os fusíveis e conexões elétricas.")
    print("Se necessário, chame um eletricista automotivo qualificado para diagnosticar e corrigir o problema.")
    return continuar_problemas()

def p_bateria():
    print("Se a bateria do carro estiver ruim, tente dar uma carga com cabos auxiliares ou um carregador portátil.")
    print("Se não resolver, substitua por uma nova ou chame um serviço de assistência para fazer isso.")
    return continuar_problemas()

def p_falt_compus():
    print("Se estiver sem combustível, pare o carro em local seguro.")
    print("Se possível, peça ajuda para trazer combustível. Se não, chame um serviço de assistência.")
    return continuar_problemas()

def p_trepidando():
    print("Se o carro estiver trepidando, verifique as rodas quanto a danos ou desequilíbrio.")
    print("Se necessário, ajuste a pressão dos pneus. Verifique os freios ou a suspensão se necessário.")
    return continuar_problemas()

def p_pneu():
    print("Se tiver um pneu furado, estacione em local seguro.")
    print("Troque o pneu ou chame um serviço de assistência para fazer isso por você.")
    return continuar_problemas()

def p_dentada():
    print("Se a correia dentada quebrar, pare o carro imediatamente para evitar danos ao motor.")
    print("Chame um serviço de reboque para levar o veículo a uma oficina mecânica.")
    return continuar_problemas()

def p_cambio():
    print("Se enfrentar problemas de câmbio, estacione com segurança.")
    print("Verifique o nível de fluido de transmissão e procure sinais de vazamento.")
    print("Se persistir, consulte um mecânico qualificado.")
    return continuar_problemas()

def funcao_menu_problemas():
    executando_chat = True
    while executando_chat:
        print("ChatBot!")
        print(menu_chat())
        problema = input("Por favor me informe o problema no seu carro: ").upper().strip()
        if problema == "S":
            executando_chat = p_superaquecimento()
        elif problema == "E":
            executando_chat = p_eletrico()
        elif problema == "B":
            executando_chat = p_bateria()
        elif problema == "F":
            executando_chat = p_falt_compus()
        elif problema == "T":
            executando_chat = p_trepidando()
        elif problema == "P":
            executando_chat = p_pneu()
        elif problema == "D":
            executando_chat = p_dentada()
        elif problema == "C":
            executando_chat = p_cambio()
        elif problema == "V":
            break
        else:
            print("Valor inválido, por favor digitar o que está entre ().")

def sair():
    print("Até Breve!")
    return False

def invalido():
    print("Opção Inválida, digite um dos números do Menu.")
    input("Aperte <ENTER> para continuar")

# Iniciando programa
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
    elif opcao == "Q":
        quem_somos()
        executando = continuar()
    elif opcao == "H":
        executando = help()
    elif opcao == "C":
        funcao_menu_problemas()
        executando = continuar()
    elif opcao == "S":
        executando = sair()
    else:
        invalido()

print("Fim do Programa!")
