import re
import json

class CRUD:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_cliente(self, nome, cpf, email, tel):
        self.validar_nome(nome)
        self.validar_cpf(cpf)
        self.validar_email(email)
        self.validar_telefone(tel)

        query = "INSERT INTO cliente (cpf_clie, nome_clie, email_clie, tel_clie) VALUES (:1, :2, :3, :4)"
        self.conexao.executar_insert_update_delete(query, [cpf, nome, email, tel])
        print(f"Cliente '{nome}' inserido com sucesso! 🎉")

    def consultar_clientes(self, cpf=None, nome=None):
        query = "SELECT * FROM cliente"
        parametros = []
        
        if cpf:
            query += " WHERE cpf_clie = :1"
            parametros.append(cpf)
        elif nome:
            query += " WHERE nome_clie LIKE :1"
            parametros.append(f"%{nome}%")
        
        
        resultados = self.conexao.executar_query(query, parametros)

        
        clientes = []
        for row in resultados:
            cliente_dict = {
                "cpf": row[0],         
                "nome": row[1],        
                "email": row[2],       
                "telefone": row[3]     
            }
            clientes.append(cliente_dict)

        return clientes

    def atualizar_cliente(self, cpf_clie, nome=None, email=None, tel=None):
        
        novos_dados = {}
        
        if nome:
            self.validar_nome(nome)
            novos_dados['nome_clie'] = nome
        if email:
            self.validar_email(email)
            novos_dados['email_clie'] = email
        if tel:
            self.validar_telefone(tel)
            novos_dados['tel_clie'] = tel

        if not novos_dados:
            print("Nenhum dado foi alterado.")
            return

        
        set_clause = ', '.join(f"{key} = :{key}" for key in novos_dados.keys())
        query = f"UPDATE cliente SET {set_clause} WHERE cpf_clie = :cpf"
        
        
        novos_dados['cpf'] = cpf_clie
        self.conexao.executar_insert_update_delete(query, novos_dados)
        print(f"Cliente com CPF '{cpf_clie}' atualizado com sucesso! 👍")

    def excluir_cliente(self, cpf_clie=None, nome_clie=None):
        if cpf_clie:
            query = "DELETE FROM cliente WHERE cpf_clie = :1"
            self.conexao.executar_insert_update_delete(query, [cpf_clie])
            print(f"Cliente com CPF '{cpf_clie}' excluído com sucesso. ❌")
        elif nome_clie:
            query = "DELETE FROM cliente WHERE nome_clie LIKE :1"
            self.conexao.executar_insert_update_delete(query, [f"%{nome_clie}%"])
            print(f"Clientes com o nome '{nome_clie}' excluídos com sucesso. ❌")

    def exportar_clientes_json(self, letra=None, file_path="clientes.json"):
        
        if letra:
            clientes = self.consultar_clientes(nome=letra)
        else:
            
            clientes = self.consultar_clientes()
        
        with open(file_path, 'w') as f:
            json.dump(clientes, f, ensure_ascii=False, indent=4)
        print(f"Dados exportados com sucesso para {file_path}. 📥")

    def validar_nome(self, nome):
        if not nome or len(nome) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres. Por favor, insira um nome válido.")
        return True

    def validar_cpf(self, cpf):
        if not re.match(r'^\d{11}$', cpf):
            raise ValueError("O CPF deve ter 11 dígitos numéricos. Por favor, insira um CPF válido.")
        return True

    def validar_email(self, email):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("O e-mail inserido não é válido. Por favor, insira um e-mail válido.")
        return True

    def validar_telefone(self, telefone):
        if not re.match(r'^\d{10,11}$', telefone):
            raise ValueError("O telefone deve ter 10 ou 11 dígitos numéricos. Por favor, insira um telefone válido.")
        return True
