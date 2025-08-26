import random
import datetime
from locust import HttpUser, task, between
from faker import Faker
fake = Faker('pt_BR')

class UsuarioTeste(HttpUser):
    wait_time = between(1, 3)  # intervalo entre requisições (segundos)        
    
    @task
    def enviar_post(self):       
        idcliente = random.randint(1, 20000)
        situacoes = ['Pendente', 'Aprovado', 'Cancelado', 'Entregue', 'Em Transporte', 'Aguardando Pagamento', 'Aguardando Retirada', 'Devolvido', 'Troca Solicitada', 'Em Análise']
        payload = {  
            "pedido": {
                "idPedidos": random.randint(20000, 90000),
                "idCliente": idcliente,
                "data": datetime.datetime.now().isoformat(),
                "situacao": random.choice(situacoes)
            },
            "cliente": {
                "idClientes": idcliente,
                "nome": fake.name(),
                "email": fake.email(),
                "telefone": fake.phone_number(),
                "dtNascimento": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
            },
            "detalhesPedido": [
                {
                "idProdutos": random.randint(1, 101000),
                "nomeProduto": "Nome do Produto 1",
                "valorProduto": round(random.uniform(50, 9999), 2),
                "quantidade": random.randint(1, 99),
                "valorUnt": round(random.uniform(50, 9999), 2)
                },
                {
                "idProdutos": random.randint(1, 101000),
                "nomeProduto": "Nome do Produto 2",
                "valorProduto": round(random.uniform(50, 9999), 2),
                "quantidade": random.randint(1, 99),
                "valorUnt": round(random.uniform(50, 9999), 2)
                }
            ]
        }
        response = self.client.post("", json=payload)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        
