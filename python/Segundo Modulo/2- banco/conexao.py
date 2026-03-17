import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()

# Cria tabela (rode uma vez, depois comente)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(100)
    )
""")

# Insere dados
data = ("Pedro", "Pedro@123.com")
cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (?, ?)",
    data
)

conexao.commit()
conexao.close()
print("✅ Dados inseridos!")