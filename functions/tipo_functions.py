import sqlite3

DB = "concessionaria.db"

def inserir_tipo(tipo, quantidade_rodas, quantidade_passageiros):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO tipo(TIPO, QUANTIDADE_RODAS, QUANTIDADE_PASSAGEIROS) VALUES ('{tipo}', {quantidade_rodas}, {quantidade_passageiros})")
    conn.commit()
