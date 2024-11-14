import sqlite3

# Criacao da tabela de animais
conn = sqlite3.connect('petshop.db')
conn.cursor().execute(''' DROP TABLE IF EXISTS animais ''')
conn.cursor().execute('''
 CREATE TABLE IF NOT EXISTS animais (
 pk_animal INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 especie TEXT NOT NULL,
 idade INTEGER NOT NULL,
 estado_adocao TEXT NOT NULL,
 adotado_por TEXT,
 adotado_em DATE
 )
''')
conn.commit()
conn.close()

# CRUD - Create | Read | Update | Delete
def inserir_animal(nome, especie, idade, estado_adocao, adotado_por=None, adotado_em=None):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        'INSERT INTO animais (nome, especie, idade, estado_adocao, adotado_por, adotado_em) VALUES (?, ?, ?, ?, ?, ?)', 
        (nome, especie, idade, estado_adocao, adotado_por, adotado_em))
    conn.commit()
    conn.close()

def inserir_animais(listaAnimais):
    for animal in listaAnimais:
        inserir_animal(*animal)

def ler_animais():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animais')
    animais = cursor.fetchall()
    conn.close()
    return animais

def atualizar_animal(animal_id, nome=None, especie=None, idade=None, estado_adocao=None):
    campos = []
    valores = []

    if nome is not None:
        campos.append("nome = ?")
        valores.append(nome)
    if especie is not None:
        campos.append("especie = ?")
        valores.append(especie)
    if idade is not None:
        campos.append("idade = ?")
        valores.append(idade)
    if estado_adocao is not None:
        campos.append("estado_adocao = ?")
        valores.append(estado_adocao)

    valores.append(animal_id)

    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute(
        f'UPDATE animais SET {", ".join(campos)} WHERE pk_animal = ?', 
        valores)
    conn.commit()
    conn.close()

def excluir_animal_por_id(animal_id):
    conn = sqlite3.connect('petshop.db')
    conn.cursor().execute('DELETE FROM animais WHERE pk_animal = ?', (animal_id,))
    conn.commit()
    conn.close()

def adotar_animal(nome_animal, adotado_por):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT estado_adocao FROM animais WHERE nome = ?', (nome_animal,))
    estado_adocao = cursor.fetchone()[0]
    if estado_adocao != 'Disponível':
        raise Exception('O animal não está disponível para adoção')
    cursor.execute(
        'UPDATE animais SET estado_adocao = "Adotado", adotado_por = ?, adotado_em = CURRENT_DATE WHERE nome = ?', 
        (adotado_por, nome_animal))
    conn.commit()
    conn.close()
