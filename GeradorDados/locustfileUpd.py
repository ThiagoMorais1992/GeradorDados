import random
import datetime
from locust import HttpUser, task, between

class UsuarioTeste(HttpUser):
    wait_time = between(1, 3)  # intervalo entre requisições (segundos)       
    
    @task
    def enviar_post(self):
        situacoes = ['Pendente', 'Aprovado', 'Cancelado', 'Entregue', 'Em Transporte', 'Aguardando Pagamento', 'Aguardando Retirada', 'Devolvido', 'Troca Solicitada', 'Em Análise']
        payload = random.choice(situacoes)
        
        response = self.client.put(random.randint(1, 1000000), json=payload)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        
