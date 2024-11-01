import oracledb
import json

class ConexaoDB:
    def __init__(self):
        self.conexao = None
        self.carregar_configuracoes()

    def carregar_configuracoes(self):
        with open('config.json') as f:
            config = json.load(f)
            self.host = config['host']
            self.port = config['port']
            self.user = config['user']
            self.password = config['password']
            self.service_name = config['service_name']

    def conectar(self):
        try:
            dsn = f"{self.host}:{self.port}/{self.service_name}"
            self.conexao = oracledb.connect(user=self.user, password=self.password, dsn=dsn)
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except oracledb.DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")

    def executar_insert_update_delete(self, query, parametros):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(query, parametros)
            self.conexao.commit()
        except oracledb.DatabaseError as e:
            print(f"Erro ao executar a operação: {e}")
            self.conexao.rollback()
        finally:
            cursor.close()
