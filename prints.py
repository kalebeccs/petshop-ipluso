from querys import *

#Cores e estilo para utilizar no terminal
white = '\033[37m'
yellow = '\033[33m'

reset_color = '\033[0;0m'
bold = '\033[1m'

# Listar todos os produtos disponíveis e as respetivas quantidades em stock
def print_listar_produtos_disponiveis():
    print(yellow+bold,"Produtos disponíveis e quantidades em stock",reset_color)
    produtos_disponiveis = listar_produtos_disponiveis()
    for produto in produtos_disponiveis:
        print(f"{white}Produto:{reset_color} {produto[0]} \n{white}Quantidade em stock:{reset_color} {produto[1]}\n")

# Consultar as compras de um cliente específico
def print_consultar_compras_cliente(nome_cliente):
    print(yellow+bold,f"Compras realizadas pelo cliente {nome_cliente}",reset_color)
    for compra in consultar_compras_cliente(nome_cliente):
        print(f"{white}Produto:{reset_color} {compra[1]} \n{white}Data da compra:{reset_color} {compra[2]} \n{white}Quantidade:{reset_color} {compra[3]} \n{white}Total:{reset_color} {compra[4]:.2f}\n")

# Listar os animais disponíveis para adoção, incluindo a espécie e a idade
def print_listar_animais_para_adocao():
    print(yellow+bold,"Animais disponíveis para adoção",reset_color)
    for animal in listar_animais_para_adocao():
        print(f"{white}Nome:{reset_color} {animal[0]} \n{white}Espécie:{reset_color} {animal[1]} \n{white}Idade:{reset_color} {animal[2]} anos\n")

# Consultar o total de compras realizadas por cada cliente
def print_consultar_total_compras_por_cliente():
    print(yellow+bold,"Total de compras realizadas por cada cliente",reset_color)
    for cliente in consultar_total_compras_por_cliente():
        print(f"{white}Cliente:{reset_color} {cliente[0]} \n{white}Total de compras:{reset_color} R${cliente[1]:.2f}\n")
