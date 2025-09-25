import sqlite3
from models import Item
from typing import List

DB_NAME = 'items.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def adicionar(item: Item) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (nome, descricao, quantidade) VALUES (?, ?, ?)",
        (item.nome, item.descricao, item.quantidade)
    )
    conn.commit()
    conn.close()

def listar_todos() -> List[Item]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items ORDER BY nome ASC")
    
    rows = cursor.fetchall()
    conn.close()
    return [
        Item(
            id=row[0], 
            nome=row[1], 
            descricao=row[2], 
            quantidade=row[3]
        ) for row in rows
    ]

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        quantidade INTEGER T NOT NULL
    );
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso.")