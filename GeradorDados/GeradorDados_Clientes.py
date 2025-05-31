from faker import Faker
from Util.Conector import conectar

fake = Faker('pt_BR')

conn = conectar()
cursor = conn.cursor()

for _ in range(20000):
    nome = fake.name()
    telefone = fake.phone_number()
    email = fake.email()
    dataN = fake.date_of_birth(minimum_age=18, maximum_age=80)
    cursor.execute("INSERT INTO clientes (nome, telefone, email, dtNascimento) VALUES (%s, %s, %s, %s)", (nome, telefone, email, dataN))

conn.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")