import json
import oracledb

class ConexaoDB:
    def __init__(self, config_file='oracle_conn.json'):
        try:
            with open(config_file, 'r') as f:
                config_list = json.load(f)
            config = config_list[0]
            self.user = config['user']
            self.password = config['password']
            self.dsn = config['dsn']
            self.connection_string = self.dsn
            self.connection = None
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {config_file}")
            raise
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
            raise
        except KeyError as e:
            print(f"Chave não encontrada no JSON: {e}")
            raise

    def connect(self):
        # Estabelece a conexão com o banco de dados.
        try:
            # Usando um dicionário para passar as credenciais
            self.connection = oracledb.connect(user=self.user, password=self.password, dsn=self.connection_string)
            print("Conexão estabelecida com sucesso!")
        except oracledb.DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def close(self):
        # Fecha a conexão com o banco de dados.
        if self.connection:
            self.connection.close()
            print("Conexão fechada.")

    def executar_query(self, query, parametros=None):
        # Executa uma consulta e retorna os resultados.
        with self.connection.cursor() as cursor:
            cursor.execute(query, parametros or [])
            resultados = cursor.fetchall()
            return resultados

    def executar_insert_update_delete(self, query, parametros=None):
        # Executa operações de inserção, atualização ou exclusão.
        with self.connection.cursor() as cursor:
            cursor.execute(query, parametros or [])
            self.connection.commit()
