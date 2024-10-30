import json
import oracledb
import os

class ConexaoDB:
    def __init__(self, config_file=None):
        self.connection = None
        self.user = None
        self.password = None
        self.dsn = None
        self.connection_string = None

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
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Erro ao carregar configurações: {e}")
            raise

    def connect(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            self.connection = oracledb.connect(user=self.user, password=self.password, dsn=self.connection_string)
            print("Conexão estabelecida com sucesso!")
        except oracledb.DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()
            print("Conexão fechada.")
            self.connection = None  # Garantir que a referência da conexão seja removida

    def _check_connection(self):
        """Verifica se a conexão está ativa. Se não, tenta conectar."""
        if self.connection is None:
            self.connect()

    def executar_query(self, query, parametros=None):
        """Executa uma consulta e retorna os resultados."""
        self._check_connection()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, parametros or [])
                resultados = cursor.fetchall()
                return resultados
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            raise

    def executar_insert_update_delete(self, query, parametros=None):
        """Executa uma operação de inserção, atualização ou exclusão."""
        self._check_connection()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, parametros or [])
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao executar a operação: {e}")
            self.connection.rollback()  # Reverter em caso de erro
            raise
