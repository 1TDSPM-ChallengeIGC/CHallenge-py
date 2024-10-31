from conexao_db import ConexaoDB
from sistema_gerenciamento import SistemaGerenciamento

def main():
    conexao = ConexaoDB()
    conexao.connect() 

    sistema = SistemaGerenciamento(conexao)
    sistema.menu_principal()

if __name__ == "__main__":
    main()
