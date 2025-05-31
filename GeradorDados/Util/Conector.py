import mysql.connector

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
    