from animais import ler_animais
from clientes import ler_clientes
from compras import ler_compras
from produtos import ler_produtos
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
        print(f"{white}Produto:{reset_color} {compra[1]} \n{white}Data da compra:{reset_color} {compra[2]} \n{white}Quantidade:{reset_color} {compra[3]} \n{white}Total:{reset_color} €{compra[4]:.2f}\n")

# Listar os animais disponíveis para adoção, incluindo a espécie e a idade
def print_listar_animais_para_adocao():
    print(yellow+bold,"Animais disponíveis para adoção",reset_color)
    for animal in listar_animais_para_adocao():
        print(f"{white}Nome:{reset_color} {animal[0]} \n{white}Espécie:{reset_color} {animal[1]} \n{white}Idade:{reset_color} {animal[2]} anos\n")

# Consultar o total de compras realizadas por cada cliente
def print_consultar_total_compras_por_cliente():
    print(yellow+bold,"Total de compras realizadas por cada cliente",reset_color)
    for cliente in consultar_total_compras_por_cliente():
        print(f"{white}Cliente:{reset_color} {cliente[0]} \n{white}Total de compras:{reset_color} €{cliente[1]:.2f}\n")

def print_ler_animais():
    print(yellow+bold,"Lista de animais",reset_color)
    for animal in ler_animais():
        print(f"{white}Nome:{reset_color} {animal[1]} \n{white}Espécie:{reset_color} {animal[2]} \n{white}Idade:{reset_color} {animal[3]} anos \n{white}Estado de adoção:{reset_color} {animal[4]}")
        if animal[4] == 'Adotado':
            print(f"{white}Adotado por:{reset_color} {animal[5]}\n{white}Adotado em:{reset_color} {animal[6]}\n")
        else:
            print("")

def print_ler_clientes():
    print(yellow+bold,"Lista de clientes",reset_color)
    for cliente in ler_clientes():
        print(f"{white}Nome:{reset_color} {cliente[1]} \n{white}Telefone:{reset_color} {cliente[2]} \n{white}Email:{reset_color} {cliente[3]} \n{white}Endereço:{reset_color} {cliente[4]}\n")

def print_ler_compras():
    print(yellow+bold,"Lista de compras",reset_color)
    for compra in ler_compras():
        print(f"{white}Cliente:{reset_color} {compra[0]} \n{white}Produto:{reset_color} {compra[1]} \n{white}Data da compra:{reset_color} {compra[2]} \n{white}Quantidade:{reset_color} {compra[3]} \n{white}Total:{reset_color} €{compra[4]:.2f}\n")

def print_ler_produtos():
    print(yellow+bold,"Lista de produtos",reset_color)
    for produto in ler_produtos():
        print(f"{white}Nome:{reset_color} {produto[1]} \n{white}Tipo:{reset_color} {produto[2]} \n{white}Preço:{reset_color} €{produto[3]:.2f} \n{white}Quantidade em stock:{reset_color} {produto[4]}\n")
