import sqlite3

# Criacao da tabela de produtos
conn = sqlite3.connect('petshop.db')
conn.cursor().execute(''' DROP TABLE IF EXISTS produtos ''')
conn.cursor().execute('''
 CREATE TABLE IF NOT EXISTS produtos (
 pk_produto INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 tipo TEXT NOT NULL,
 preco REAL NOT NULL,
 quantidade_stock INTEGER NOT NULL
 )
''')
conn.commit()
conn.close()

# CRUD - Create | Read | Update | Delete
def inserir_produto(nome, tipo, preco, quantidade_stock):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        'INSERT INTO produtos (nome, tipo, preco, quantidade_stock) VALUES (?, ?, ?, ?)', 
        (nome, tipo, preco, quantidade_stock))
    conn.commit()
    conn.close()


def inserir_produtos(listaProdutos):
    for produto in listaProdutos:
        inserir_produto(*produto)

def ler_produtos():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def atualizar_produto_por_id(produto_id, nome=None, tipo=None, preco=None, quantidade_stock=None):
    campos = []
    valores = []

    if nome is not None:
        campos.append("nome = ?")
        valores.append(nome)
    if tipo is not None:
        campos.append("tipo = ?")
        valores.append(tipo)
    if preco is not None:
        campos.append("preco = ?")
        valores.append(preco)
    if quantidade_stock is not None:
        campos.append("quantidade_stock = ?")
        valores.append(quantidade_stock)

    valores.append(produto_id)

    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        f'UPDATE produtos SET {', '.join(campos)} WHERE pk_produto = ?', 
        valores)
    conn.commit()
    conn.close()

def atualizar_produto_por_nome(nome, tipo=None, preco=None, quantidade_stock=None):
    campos = []
    valores = []

    if tipo is not None:
        campos.append("tipo = ?")
        valores.append(tipo)
    if preco is not None:
        campos.append("preco = ?")
        valores.append(preco)
    if quantidade_stock is not None:
        campos.append("quantidade_stock = ?")
        valores.append(quantidade_stock)

    valores.append(nome)

    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        f'UPDATE produtos SET {', '.join(campos)} WHERE nome = ?', 
        valores)
    conn.commit()
    conn.close()


def excluir_produto_por_id(produto_id):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute('DELETE FROM produtos WHERE pk_produto = ?', (produto_id,))
    conn.commit()
    conn.close()
