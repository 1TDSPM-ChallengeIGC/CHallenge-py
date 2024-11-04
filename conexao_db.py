import json
import oracledb
import os

class ConexaoDB:
    def __init__(self):
        self.carregar_configuracoes()
        self.conexao = None  

    def carregar_configuracoes(self):
        # Get the directory of the current script
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(dir_path, 'config.json')

        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            self.user = config.get('user')
            self.password = config.get('password')
            self.dsn = config.get('dsn')

            if not all([self.user, self.password, self.dsn]):
                raise ValueError("Configurações de conexão incompletas.")

    def connect(self):
        try:
            self.conexao = oracledb.connect(user=self.user, password=self.password, dsn=self.dsn)
            print("Conexão estabelecida com sucesso! 🎉")
        except oracledb.DatabaseError as e:
            error, = e.args
            print("Erro ao conectar ao banco de dados:", error.message)

    def close(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão encerrada. 👋")

    def executar_consulta(self, consulta, parametros=None):
        with self.conexao.cursor() as cursor:
            cursor.execute(consulta, parametros or [])
            return cursor.fetchall()

    def executar_comando(self, comando, parametros=None):
        with self.conexao.cursor() as cursor:
            cursor.execute(comando, parametros or [])
            self.conexao.commit()
