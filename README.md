<div align="">
  <img src="logo.jpg" alt="Logo do Lojão da Ração" width="220"/>
</div>

# Lojão da Ração

**Lojão da Ração** é um sistema de gerenciamento para petshops, desenvolvido em Python com uso do SQLite3. Este projeto permite a administração de produtos, clientes, animais disponíveis para adoção e o registro de compras.

## 🚀 Funcionalidades

- **Gestão de Produtos:** Adicionar, atualizar, remover e listar produtos, com controle de estoque e categorias.
- **Cadastro de Clientes:** Inserção e consulta dos dados dos clientes.
- **Registro de Animais para Adoção:** Armazenamento e gerenciamento de dados dos animais, incluindo status de adoção.
- **Controle de Compras:** Registro e consulta de compras realizadas pelos clientes, com cálculo de totais.
- **Relatórios de Dados:** Consultas personalizadas para listagem de produtos, animais disponíveis, compras por cliente e totais de compra.

## 📂 Estrutura do Projeto

- `clientes.py` - Operações CRUD para a tabela de clientes.
- `produtos.py` - Operações CRUD para a tabela de produtos.
- `animais.py` - Operações CRUD para a tabela de animais para adoção.
- `compras.py` - Operações CRUD para a tabela de compras.
- `querys.py` - Funções para consultas específicas no banco de dados. 
- `prints.py` - Funções de exibição no terminal.
- `main.py` - Arquivo principal para execução das funcionalidades.

## 💻 Requisitos

- Python 3.6 ou superior
- Biblioteca `sqlite3` (inclusa na instalação padrão do Python)

## 🔧 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seuusuario/Lojao-da-Racao.git
   cd Lojao-da-Racao
   ```

2. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

3. Siga as instruções no terminal para gerenciar os dados do sistema.

## 📋 Exemplo de Uso

- **Adicionar Produto:** Insere novos produtos no estoque, com nome, tipo, preço e quantidade.
- **Consulta de Compras:** Verifica as compras realizadas por um cliente específico, incluindo detalhes de cada transação.
- **Adoção de Animais:** Atualiza o estado de adoção de um animal ao ser adotado por um cliente.
- **Listagem de Produtos Disponíveis:** Mostra todos os produtos em estoque com suas quantidades.

## 🤝 Contribuidores

Agradecimentos aos contribuidores deste projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/kalebeccs">
        <img src="https://github.com/kalebeccs.png" width="100px;" alt="Eliesr Santos"/>
        <br />
        <sub><b>Eliesr Santos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ffvitor">
        <img src="https://github.com/ffvitor.png" width="100px;" alt="Vitor Ferreira"/>
        <br />
        <sub><b>Vitor Ferreira</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/caroliinesousa">
        <img src="https://github.com/caroliinesousa.png" width="100px;" alt="Ana Sousa"/>
        <br />
        <sub><b>Ana Sousa</b></sub>
      </a>
    </td>
  </tr>
</table>
