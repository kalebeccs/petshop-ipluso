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
    conn.cursor().execute('SELECT * FROM compras')
    compras = conn.cursor().fetchall()
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
