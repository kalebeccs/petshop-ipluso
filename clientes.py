import sqlite3

# Criação da tabela de clientes
conn = sqlite3.connect('petshop.db')
conn.cursor().execute(''' DROP TABLE IF EXISTS clientes ''')
conn.cursor().execute('''
 CREATE TABLE IF NOT EXISTS clientes (
 pk_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 telefone TEXT NOT NULL,
 email TEXT NOT NULL,
 endereco TEXT NOT NULL
 )
''')
conn.commit()
conn.close()

# CRUD - Create | Read | Update | Delete para clientes
def inserir_cliente(nome, telefone, email, endereco):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        'INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)', 
        (nome, telefone, email, endereco))
    conn.commit()
    conn.close()

def inserir_clientes(listaClientes):
    for cliente in listaClientes:
        inserir_cliente(*cliente)

def ler_clientes():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def atualizar_cliente(cliente_id, nome=None, telefone=None, email=None, endereco=None):
    campos = []
    valores = []

    if nome is not None:
        campos.append("nome = ?")
        valores.append(nome)
    if telefone is not None:
        campos.append("telefone = ?")
        valores.append(telefone)
    if email is not None:
        campos.append("email = ?")
        valores.append(email)
    if endereco is not None:
        campos.append("endereco = ?")
        valores.append(endereco)

    valores.append(cliente_id)

    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        f'UPDATE clientes SET {", ".join(campos)} WHERE pk_cliente = ?', 
        valores)
    conn.commit()
    conn.close()

def excluir_cliente_por_id(cliente_id):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute('DELETE FROM clientes WHERE pk_cliente = ?', (cliente_id,))
    conn.commit()
    conn.close()
