from datetime import date

from clientes import *
from produtos import *
from animais import *
from compras import *
from prints import *

# Dados para inserção nas tabelas
produtos = [
    # (nome, tipo, preco, quantidade_stock)
    ('Ração Premium', 'Ração', 89.90, 20),
    ('Brinquedo Mordedor', 'Brinquedo', 29.90, 50),
    ('Coleira Ajustável', 'Acessório', 19.90, 30),
    ('Shampoo para Cães', 'Higiene', 25.00, 15),
    ('Casinha para Cachorros', 'Acessório', 199.90, 10)
]
clientes = [
    # (nome, telefone, email, endereco)
    ('Carlos Souza', '1234567890', 'carlos@gmail.com', 'Rua A, 123'),
    ('Ana Martins', '0987654321', 'ana@gmail.com', 'Rua B, 456'),
    ('João Silva', '1122334455', 'joao@gmail.com', 'Rua C, 789'),
    ('Mariana Costa', '5566778899', 'mariana@gmail.com', 'Rua D, 321'),
    ('Lucas Oliveira', '6677889900', 'lucas@gmail.com', 'Rua E, 654')
]
animais = [
    # (nome, especie, idade, estado_adocao)
    ('Bobby', 'Cachorro', 3, 'Disponível'),
    ('Mimi', 'Gato', 2, 'Adotado'),
    ('Nina', 'Cachorro', 1, 'Disponível')
]
compras = [
    # (fk_cliente, fk_produto, data_compra, quantidade, total)
    (1, 1, date(2024, 10, 1), 2, 179.80),
    (2, 2, date(2024, 10, 3), 1, 29.90),
    (3, 3, date(2024, 10, 5), 1, 19.90),
    (4, 4, date(2024, 10, 7), 3, 75.00),
    (5, 5, date(2024, 10, 10), 1, 199.90)
]

# Inserindo os dados com um for loop para cada tabela
inserir_produtos(produtos)
inserir_clientes(clientes)
inserir_animais(animais)
inserir_compras(compras)

# Atualizando um produto
atualizar_produto(1,'Ração Golden')

# Listar todos os produtos disponíveis e as respetivas quantidades em stock
print_listar_produtos_disponiveis()

# Consultar as compras de um cliente específico
nome_cliente = "Carlos Souza"
print_consultar_compras_cliente(nome_cliente)

# Listar os animais disponíveis para adoção, incluindo a espécie e a idade
print_listar_animais_para_adocao()

# Consultar o total de compras realizadas por cada cliente
print_consultar_total_compras_por_cliente()
