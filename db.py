import sqlite3

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
        self.cursor.
    def edit():
        print("a")

    def remove():
        print("a")