import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,lote INTEGER NOT NULL,nota_fiscal TEXT,validade DATE NOT NULL, quantidade INTEGER NOT NULL)")

