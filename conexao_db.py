import json
import oracledb
import os

class ConexaoDB:
    def __init__(self, config_file=None):
        try:
            if not config_file:
                base_dir = os.path.dirname(__file__)
                config_file = os.path.join(base_dir, "oracle_conn.json")
            if not os.path.exists(config_file):
                raise FileNotFoundError(f"Erro: Arquivo '{config_file}' não encontrado.")
           
            with open(config_file, 'r') as f:
                config_list = json.load(f)
            config = config_list[0]
            self.user = config['user']
            self.password = config['password']
            self.dsn = config['dsn']
            self.connection_string = self.dsn
            self.connection = None
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Erro ao carregar configurações: {e}")
            raise
 
    def connect(self):
        try:
            self.connection = oracledb.connect(user=self.user, password=self.password, dsn=self.connection_string)
            print("Conexão estabelecida com sucesso! Vamos começar.")
        except oracledb.DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise
 
    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão encerrada. Até a próxima!")
 
    def executar_query(self, query, parametros=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, parametros or [])
            resultados = cursor.fetchall()
            return resultados
 
    def executar_insert_update_delete(self, query, parametros=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, parametros or [])
            self.connection.commit()
