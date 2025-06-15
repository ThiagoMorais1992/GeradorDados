import mysql.connector
from pymongo import MongoClient

def conectar():
    # Conexão com o banco de dados
    try:
        conn = mysql.connector.connect(user='root', password='123456', database='lojavirtual_mdb', host='localhost')
        if conn.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None 

def ConectarMongo():
    # Conexão com o banco de dados MongoDB    
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['LojaVirtual_mdb']
        print("Conexão com o MongoDB estabelecida com sucesso!")
        return db, client
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None    