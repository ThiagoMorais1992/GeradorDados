from faker import Faker
from Util.Conector import conectar
import random

fake = Faker('pt_BR')

conn = conectar()
cursor = conn.cursor()
situacoes = ['Pendente', 'Aprovado', 'Cancelado', 'Entregue', 'Em Transporte', 'Aguardando Pagamento', 'Aguardando Retirada', 'Devolvido', 'Troca Solicitada', 'Em Análise']

for _ in range(1000000):
    
    idcliente = fake.random_int(min=1, max=20000)
    data = fake.date_between(start_date='-10y', end_date='today')
    situacao = random.choice(situacoes)
    cursor.execute("INSERT INTO pedidos (idcliente, data, situacao) VALUES (%s, %s, %s)", (idcliente, data, situacao))

conn.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")