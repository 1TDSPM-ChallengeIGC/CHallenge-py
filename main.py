from sistema_gerenciamento import SistemaGerenciamento

def main():
    sistema = SistemaGerenciamento()
    
    
    sistema.conexao.connect()
    
    try:
       
        sistema.menu_principal()
    finally:
       
        sistema.conexao.close()

if __name__ == "__main__":
    main()