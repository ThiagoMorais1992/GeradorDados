import random
import datetime
from locust import HttpUser, task, between

class UsuarioTeste(HttpUser):
    wait_time = between(1, 3)  # intervalo entre requisições (segundos)       
    
    @task
    def enviar_post(self):
        situacoes = ['Pendente', 'Aprovado', 'Cancelado', 'Entregue', 'Em Transporte', 'Aguardando Pagamento', 'Aguardando Retirada', 'Devolvido', 'Troca Solicitada', 'Em Análise']
        payload = {   
            "idpedido": None,                 
            "idcliente": random.randint(1, 20000),
            "data": datetime.datetime.now().isoformat(),
            "situacao": random.choice(situacoes),
            "detalhes": [
                {                        
                "produto": {
                    "idprodutos": random.randint(1, 101000)
                },
                "quantidade": random.randint(1, 99),
                "valor_unt": round(random.uniform(50, 9999), 2)
                },
                {                        
                "produto": {
                    "idprodutos": random.randint(1, 1000)
                },
                "quantidade": random.randint(1, 99),
                "valor_unt": round(random.uniform(50, 9999), 2)
                }
            ]	
        }
        response = self.client.post("", json=payload)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        
