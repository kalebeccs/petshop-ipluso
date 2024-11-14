import sqlite3

# Função para listar todos os produtos disponíveis e as respectivas quantidades em stock
def listar_produtos_disponiveis():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, quantidade_stock FROM produtos')
    produtosDisponiveis = cursor.fetchall()
    conn.close()
    return produtosDisponiveis

# Função para consultar as compras de um cliente específico
def consultar_compras_cliente(nome_cliente):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.nome, p.nome, cp.data_compra, cp.quantidade, cp.total
        FROM compras cp
        JOIN clientes c ON cp.fk_cliente = c.pk_cliente
        JOIN produtos p ON cp.fk_produto = p.pk_produto
        WHERE c.nome = ?
    ''', (nome_cliente,))
    comprasCliente = cursor.fetchall()
    conn.close()
    return comprasCliente

# Função para listar os animais disponíveis para adoção, incluindo a espécie e a idade
def listar_animais_para_adocao():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, especie, idade FROM animais WHERE estado_adocao = "Disponível"')
    animaisDisponiveis = cursor.fetchall()
    conn.close()
    return animaisDisponiveis

# Função para consultar o total de compras realizadas por cada cliente
def consultar_total_compras_por_cliente():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.nome, SUM(cp.total) AS total_compras
        FROM compras cp
        JOIN clientes c ON cp.fk_cliente = c.pk_cliente
        GROUP BY c.nome
    ''')
    totalCompras = cursor.fetchall()
    conn.close()
    return totalCompras
