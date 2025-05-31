from faker import Faker
from Util.Conector import conectar
import random

fake = Faker('pt_BR')

conn = conectar()
cursor = conn.cursor()


for _ in range(5000000):
    idpedido = fake.random_int(min=1, max=1000000)
    idproduto = fake.random_int(min=1, max=100000)
    quantidade = fake.random_int(min=1, max=20)
    valor_unt = round(random.uniform(50, 9999), 2)
    cursor.execute("INSERT INTO detalhe_pedido (idpedido, idproduto, quantidade, valor_unt) VALUES (%s, %s, %s, %s)", (idpedido, idproduto, quantidade, valor_unt))


conn.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")