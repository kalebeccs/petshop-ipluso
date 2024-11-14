import sqlite3

# Criacao da tabela de compras
conn = sqlite3.connect('petshop.db')
conn.cursor().execute(''' DROP TABLE IF EXISTS compras ''')
conn.cursor().execute('''
 CREATE TABLE IF NOT EXISTS compras (
 pk_compra INTEGER PRIMARY KEY AUTOINCREMENT,
 fk_cliente INTEGER NOT NULL,
 fk_produto INTEGER NOT NULL,
 data_compra DATE NOT NULL,
 quantidade INTEGER NOT NULL,
 total REAL NOT NULL,
 FOREIGN KEY (fk_cliente) REFERENCES clientes(pk_cliente),
 FOREIGN KEY (fk_produto) REFERENCES produtos(pk_produto)
 )
''')
conn.commit()
conn.close()

# CRUD - Create | Read | Update | Delete
def inserir_compra(fk_cliente, fk_produto, data_compra, quantidade, total):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        'INSERT INTO compras (fk_cliente, fk_produto, data_compra, quantidade, total) VALUES (?, ?, ?, ?, ?)', 
        (fk_cliente, fk_produto, data_compra, quantidade, total))
    conn.commit()
    conn.close()

def inserir_compras(listaCompras):
    for compra in listaCompras:
        inserir_compra(*compra)

def ler_compras():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT clientes.nome, produtos.nome,data_compra, quantidade, total FROM compras
                    JOIN clientes ON compras.fk_cliente = clientes.pk_cliente
                    JOIN produtos ON compras.fk_produto = produtos.pk_produto
                   ''')
    compras = cursor.fetchall()
    conn.close()
    return compras

def atualizar_compra(compra_id, fk_cliente=None, fk_produto=None, data_compra=None, quantidade=None, total=None):
    campos = []
    valores = []

    if fk_cliente is not None:
        campos.append("fk_cliente = ?")
        valores.append(fk_cliente)
    if fk_produto is not None:
        campos.append("fk_produto = ?")
        valores.append(fk_produto)
    if data_compra is not None:
        campos.append("data_compra = ?")
        valores.append(data_compra)
    if quantidade is not None:
        campos.append("quantidade = ?")
        valores.append(quantidade)
    if total is not None:
        campos.append("total = ?")
        valores.append(total)

    valores.append(compra_id)

    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        f'UPDATE compras SET {", ".join(campos)} WHERE pk_compra = ?', 
        valores)
    conn.commit()
    conn.close()

def excluir_compra_por_id(compra_id):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute('DELETE FROM compras WHERE pk_compra = ?', (compra_id,))
    conn.commit()
    conn.close()

# Função para comprar um produto
def comprar_produto(nome_cliente, nome_produto, data_compra, quantidade):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT pk_cliente FROM clientes WHERE nome = ?', (nome_cliente,))
    cliente = cursor.fetchone()
    if cliente is None:
        print('Cliente não encontrado')
        return
    cliente_id = cliente[0]
    cursor.execute('SELECT pk_produto FROM produtos WHERE nome = ?', (nome_produto,))
    produto = cursor.fetchone()
    if produto is None:
        print('Produto não encontrado')
        return
    produto_id = produto[0]
    cursor.execute('SELECT preco, quantidade_stock FROM produtos WHERE pk_produto = ?', (produto_id,))
    produto = cursor.fetchone()
    preco = produto[0]
    quantidade_stock = produto[1]
    total = preco * quantidade
    if quantidade_stock >= quantidade:
        conn.cursor().execute(
            'INSERT INTO compras (fk_cliente, fk_produto, data_compra, quantidade, total) VALUES (?, ?, ?, ?, ?)', 
            (cliente_id, produto_id, data_compra, quantidade, total))
        conn.cursor().execute(
            'UPDATE produtos SET quantidade_stock = ? WHERE pk_produto = ?', 
            (quantidade_stock - quantidade, produto_id))
        conn.commit()
    conn.close()
