import sqlite3
from datetime import date

conn = sqlite3.connect('petshop.db')
cursor = conn.cursor()

# Criação das tabelas
cursor.execute(''' DROP TABLE IF EXISTS produtos ''')
cursor.execute('''
 CREATE TABLE IF NOT EXISTS produtos (
 pk_produto INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 tipo TEXT NOT NULL,
 preco REAL NOT NULL,
 quantidade_stock INTEGER NOT NULL
 )
''')
cursor.execute(''' DROP TABLE IF EXISTS clientes ''')
cursor.execute('''
 CREATE TABLE IF NOT EXISTS clientes (
 pk_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 telefone TEXT NOT NULL,
 email TEXT NOT NULL,
 endereco TEXT NOT NULL
 )
''')
cursor.execute(''' DROP TABLE IF EXISTS animais ''')
cursor.execute('''
 CREATE TABLE IF NOT EXISTS animais (
 pk_animal INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 especie TEXT NOT NULL,
 idade INTEGER NOT NULL,
 estado_adocao TEXT NOT NULL
 )
''')
cursor.execute(''' DROP TABLE IF EXISTS compras ''')
cursor.execute('''
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

# Funções de inserção para cada entrada individual
def inserir_produto(nome, tipo, preco, quantidade_stock):
    cursor.execute('INSERT INTO produtos (nome, tipo, preco, quantidade_stock) VALUES (?, ?, ?, ?)', (nome, tipo, preco, quantidade_stock))

def inserir_cliente(nome, telefone, email, endereco):
    cursor.execute('INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)', (nome, telefone, email, endereco))

def inserir_animal(nome, especie, idade, estado_adocao):
    cursor.execute('INSERT INTO animais (nome, especie, idade, estado_adocao) VALUES (?, ?, ?, ?)', (nome, especie, idade, estado_adocao))

def inserir_compra(fk_cliente, fk_produto, data_compra, quantidade, total):
    cursor.execute('INSERT INTO compras (fk_cliente, fk_produto, data_compra, quantidade, total) VALUES (?, ?, ?, ?, ?)', (fk_cliente, fk_produto, data_compra, quantidade, total))

# Dados para inserção nas tabelas
produtos = [
    ('Ração Premium', 'Ração', 89.90, 20),
    ('Brinquedo Mordedor', 'Brinquedo', 29.90, 50),
    ('Coleira Ajustável', 'Acessório', 19.90, 30),
    ('Shampoo para Cães', 'Higiene', 25.00, 15),
    ('Casinha para Cachorros', 'Acessório', 199.90, 10)
]
clientes = [
    ('Carlos Souza', '1234567890', 'carlos@gmail.com', 'Rua A, 123'),
    ('Ana Martins', '0987654321', 'ana@gmail.com', 'Rua B, 456'),
    ('João Silva', '1122334455', 'joao@gmail.com', 'Rua C, 789'),
    ('Mariana Costa', '5566778899', 'mariana@gmail.com', 'Rua D, 321'),
    ('Lucas Oliveira', '6677889900', 'lucas@gmail.com', 'Rua E, 654')
]
animais = [
    ('Bobby', 'Cachorro', 3, 'Disponível'),
    ('Mimi', 'Gato', 2, 'Adotado'),
    ('Nina', 'Cachorro', 1, 'Disponível')
]
compras = [
    (1, 1, date(2024, 10, 1), 2, 179.80),
    (2, 2, date(2024, 10, 3), 1, 29.90),
    (3, 3, date(2024, 10, 5), 1, 19.90),
    (4, 4, date(2024, 10, 7), 3, 75.00),
    (5, 5, date(2024, 10, 10), 1, 199.90)
]

# Inserindo os dados com um for loop para cada tabela
for produto in produtos:
    inserir_produto(*produto)

for cliente in clientes:
    inserir_cliente(*cliente)

for animal in animais:
    inserir_animal(*animal)

for compra in compras:
    inserir_compra(*compra)

conn.commit()

# Função para listar todos os produtos disponíveis e as respectivas quantidades em stock
def listar_produtos_disponiveis():
    cursor.execute('SELECT nome, quantidade_stock FROM produtos')
    return cursor.fetchall()

# Função para consultar as compras de um cliente específico
def consultar_compras_cliente(nome_cliente):
    cursor.execute('''
        SELECT c.nome, p.nome, cp.data_compra, cp.quantidade, cp.total
        FROM compras cp
        JOIN clientes c ON cp.fk_cliente = c.pk_cliente
        JOIN produtos p ON cp.fk_produto = p.pk_produto
        WHERE c.nome = ?
    ''', (nome_cliente,))
    return cursor.fetchall()

# Função para listar os animais disponíveis para adoção, incluindo a espécie e a idade
def listar_animais_para_adocao():
    cursor.execute('SELECT nome, especie, idade FROM animais WHERE estado_adocao = "Disponível"')
    return cursor.fetchall()

# Função para consultar o total de compras realizadas por cada cliente
def consultar_total_compras_por_cliente():
    cursor.execute('''
        SELECT c.nome, SUM(cp.total) AS total_compras
        FROM compras cp
        JOIN clientes c ON cp.fk_cliente = c.pk_cliente
        GROUP BY c.nome
    ''')
    return cursor.fetchall()

#Cores e estilo para utilizar no terminal
white = '\033[37m'
yellow = '\033[33m'
reset_color = '\033[0;0m'
bold = '\033[1m'

# Listar todos os produtos disponíveis e as respetivas quantidades em stock
produtos_disponiveis = listar_produtos_disponiveis()
print(yellow+bold,"Produtos disponíveis e quantidades em stock",reset_color)
for produto in produtos_disponiveis:
    print(f"{white}Produto:{reset_color} {produto[0]} \n{white}Quantidade em stock:{reset_color} {produto[1]}\n")

# Consultar as compras de um cliente específico
nome_cliente = "Carlos Souza"
compras_cliente = consultar_compras_cliente(nome_cliente)
print(yellow+bold,f"Compras realizadas pelo cliente {nome_cliente}",reset_color)
for compra in compras_cliente:
    print(f"{white}Produto:{reset_color} {compra[1]} \n{white}Data da compra:{reset_color} {compra[2]} \n{white}Quantidade:{reset_color} {compra[3]} \n{white}Total:{reset_color} {compra[4]:.2f}\n")

# Listar os animais disponíveis para adoção, incluindo a espécie e a idade
animais_adocao = listar_animais_para_adocao()
print(yellow+bold,"Animais disponíveis para adoção",reset_color)
for animal in animais_adocao:
    print(f"{white}Nome:{reset_color} {animal[0]} \n{white}Espécie:{reset_color} {animal[1]} \n{white}Idade:{reset_color} {animal[2]} anos\n")

# Consultar o total de compras realizadas por cada cliente
totais_compras_clientes = consultar_total_compras_por_cliente()
print(yellow+bold,"Total de compras realizadas por cada cliente",reset_color)
for cliente in totais_compras_clientes:
    print(f"{white}Cliente:{reset_color} {cliente[0]} \n{white}Total de compras:{reset_color} R${cliente[1]:.2f}\n")

conn.close()
