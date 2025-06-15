import random
from locust import HttpUser, task, between

class UsuarioTeste(HttpUser):
    wait_time = between(1, 3)  # intervalo entre requisições (segundos)    

    @task
    def chamada_api(self):
        numero = random.randint(1, 1000000)
        self.client.get(f"{numero}") 
        
