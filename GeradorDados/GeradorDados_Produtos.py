from faker import Faker
from Util.Conector import conectar
import random

conn = conectar()
cursor = conn.cursor()

fake = Faker('pt_BR')

categorias = ['Mouse', 'Teclado', 'Fone', 'Câmera', 'Notebook', 'Monitor', 'Celular', 'Tablet', 'Impressora', 'Roteador', 'Webcam', 'Pendrive', 'HD Externo', 'SSD', 'Placa de Vídeo', 'Placa Mãe']
marcas = ['Logitech', 'Samsung', 'Dell', 'HP', 'Sony', 'Apple', 'Asus', 'Acer', 'Lenovo', 'Microsoft', 'Corsair', 'Razer', 'Kingston', 'Seagate', 'Western Digital', 'Intel', 'AMD']
modelos = [fake.word() for _ in range(100)]

def gerar_nome_produto():
    categoria = random.choice(categorias)
    marca = random.choice(marcas)
    modelo = random.choice(modelos).capitalize()
    return f"{categoria} {marca} {modelo}"

for _ in range(100000):
    nome = gerar_nome_produto()
    valor = round(random.uniform(50, 9999), 2)
    cursor.execute("INSERT INTO produtos (nome, valor) VALUES (%s, %s)", (nome, valor))

conn.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")