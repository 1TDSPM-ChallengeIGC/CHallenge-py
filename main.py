from sistema_gerenciamento import SistemaGerenciamento

def main():
    sistema = SistemaGerenciamento()
    
    # Conectar ao banco de dados
    sistema.conexao.connect()
    
    try:
        # Iniciar o menu principal do sistema
        sistema.menu_principal()
    finally:
        # Fechar a conexão com o banco de dados ao finalizar
        sistema.conexao.close()

if __name__ == "__main__":
    main()
