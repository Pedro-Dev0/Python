import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()


# Cria tabela (rode uma vez, depois comente)
def criar_tabela(conexao, cursor):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(100)
        )
    """)
    conexao.commit()
    print("✅ Tabela criada!")


# Insere dados
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT OR IGNORE INTO clientes (nome, email) VALUES (?,?)", data)
    conexao.commit()
    print("✅ Dados inseridos!")


def atualizar_registro(conexao, cursor, nome, email, id):
    update = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", update)
    conexao.commit()
    print("✅ Dados atualizados!")

def excluir_registro(conexao, cursor, id):
    excluir = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", excluir)
    conexao.commit()
    print("✅ Dados deletados!")

def inserir_registros(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()
    conexao.close()
    print("✅ Dados inseridos!")



atualizar_registro(
    conexao,
    cursor,
    "Lara",
    "Lara@gamil",
    4,
)

#excluir_registro(conexao, cursor, 9)

"""dados = [
    ("Rubens", "rubens@gmail.com"),
    ("Gimenes", "Ximenes@gmail.com"),
    ("Isabela", "isabela@gmail.com"),
    ("Rafaela", "rafaela@gmail.com"),
]

inserir_registros(conexao, cursor, dados)
"""
