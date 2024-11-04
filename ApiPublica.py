
import requests

class ApiPublica:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/users"

    def obter_usuarios(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()  
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None

    def exibir_usuarios(self):
        usuarios = self.obter_usuarios()
        if usuarios:
            for usuario in usuarios:
                print(f"Nome: {usuario['name']}, Email: {usuario['email']}")
        else:
            print("Nenhum usuário encontrado.")
