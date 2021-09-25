import sqlite3
from sqlite3 import *
from sqlite3 import Cursor

class Database:
    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nomeProduto text, nomeMarca text, valorProduto text)")
    
    def get(self):
        self.cursor.execute("SELECT * from produtos")
        rows = self.cursor.fetchall()
        return rows

    def add(self, nomeProduto, nomeMarca, valorProduto):
        self.cursor.execute("INSERT INTO produtos VALUES (NULL, ?, ?, ?)", (nomeProduto, nomeMarca, valorProduto))
        self.connect.commit()

    def edit(self, id, nomeProduto, nomeMarca, valorProduto):
        self.cursor.execute("UPDATE produtos SET nomeProduto = ?, nomeMarca = ?, valorProduto = ? WHERE id = ?",
        (nomeProduto, nomeMarca, valorProduto, id))
        self.connect.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM produtos WHERE ID = ?", (id,))
        self.connect.commit()
    
    def __delattr__(self, name: str) -> None:
        self.connect.close()