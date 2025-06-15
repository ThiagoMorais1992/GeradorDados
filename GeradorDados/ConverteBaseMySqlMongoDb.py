from Util.Conector import conectar, ConectarMongo
import datetime
import decimal

class PedidoDetalhe:
    def __init__(self, idprodutos, nome_produto, valor_produto, quantidade, valor_unt,):
        self.idprodutos = idprodutos
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.quantidade = quantidade
        self.valor_unt = valor_unt

class Cliente:
    def __init__(self, idclientes, nome, email, telefone, dtNascimento):
        self.idclientes = idclientes
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.dtNascimento = dtNascimento

class Pedido:
    def __init__(self, idpedidos, idcliente, data, situacao):
        self.idpedidos = idpedidos
        self.idcliente = idcliente
        self.data = data
        self.situacao = situacao

conn = conectar()
cursor = conn.cursor()
db, client = ConectarMongo()

lstPedidos = []
rangeInicio = 18590
rangeFim = rangeInicio + 500

while rangeFim + 1 <= 1000500:
    print(f"Processando pedidos entre {rangeInicio} e {rangeFim}...".format(rangeInicio=rangeInicio, rangeFim=rangeFim))
    consulta = "Select "\
                "p.idpedidos, p.idcliente, p.data, p.situacao, "\
                "cli.nome, cli.email, cli.telefone, cli.dtNascimento, "\
                "dp.quantidade, dp.valor_unt,"\
                "prd.idprodutos, prd.nome, prd.valor "\
                "from detalhe_pedido dp "\
                "join pedidos p on (dp.idpedido = p.idpedidos)  "\
                "join produtos prd on (dp.idproduto = prd.idprodutos)  "\
                "join clientes cli on (p.idcliente = cli.idclientes) "\
                "WHERE p.idpedidos between {rageInicio} and {rangeFim} "\
                "ORDER BY p.idpedidos ".format(rageInicio=rangeInicio, rangeFim=rangeFim) 
    cursor.execute(consulta)

    # Pegando todos os resultados
    resultados = cursor.fetchall()

    detalhes_pedido = []

    inicioPedido = True
    ultPedido = 0
    for linha in resultados:

        if ultPedido != linha[0]:
            inicioPedido = True
            
            if ultPedido != 0:
                print(f"Pedido {ultPedido} processado com sucesso!")
                # Adiciona o pedido ao dicionário     
                doc = ({
                    "pedido": pedido.__dict__,
                    "cliente": cliente.__dict__,
                    "detalhes_pedido": [dp.__dict__ for dp in detalhes_pedido]
                })
                lstPedidos.append(doc)
                detalhes_pedido.clear()
                cliente = None
                pedido = None
                detalhe_pedido = None
        
        if inicioPedido:
            print(f"Processando dados do pedido {linha[0]}...")
            inicioPedido = False
            cliente = Cliente(
                idclientes=linha[1],
                nome=linha[4],
                email=linha[5],
                telefone=linha[6],
                dtNascimento=datetime.datetime.combine(linha[7], datetime.time.min) if isinstance(linha[7], datetime.date) else linha[7]
            )
            pedido = Pedido(    
                idpedidos=linha[0],
                idcliente=linha[1],
                data=datetime.datetime.combine(linha[2], datetime.time.min) if isinstance(linha[2], datetime.date) else linha[2],
                situacao=linha[3]
            )
        
        detalhe_pedido = PedidoDetalhe(
            idprodutos=linha[10],
            nome_produto=linha[11],
            valor_produto=float(linha[12]) if isinstance(linha[12], decimal.Decimal) else linha[12],
            quantidade=int(linha[8]),
            valor_unt=float(linha[9]) if isinstance(linha[9], decimal.Decimal) else linha[9]
        )
        detalhes_pedido.append(detalhe_pedido)
        ultPedido = linha[0]
    
    print(f"Pedido {ultPedido} processado com sucesso!")
    # Adiciona o pedido ao dicionário     
    doc = ({
        "pedido": pedido.__dict__,
        "cliente": cliente.__dict__,
        "detalhes_pedido": [dp.__dict__ for dp in detalhes_pedido]
    })
    lstPedidos.append(doc)
    
    print(f"Total de pedidos processados: {len(lstPedidos)} inserindo no MongoDB.")
    try:
        db.Pedidos.insert_many(lstPedidos)
    except Exception as e:
        print(f"Erro ao inserir pedidos no MongoDB: {e}")
    
    lstPedidos.clear()
    detalhes_pedido.clear()
    detalhes_pedido.clear()
    cliente = None
    pedido = None
    detalhe_pedido = None
    rangeInicio = rangeFim + 1
    rangeFim += 500      
    print(f"Pedidos entre {rangeInicio} e {rangeFim} processados com sucesso!")
    
  
print(f"Pedido {pedido.idpedidos} inserido com sucesso no MongoDB!")

cursor.close()
conn.close()
client.close()