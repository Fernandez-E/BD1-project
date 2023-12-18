import sqlite3

conn = sqlite3.connect("concessionaria.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO veiculo (ID_VEICULO, MODELO, ID_TIPO, ID_MONTADORA, ANO, POTENCIA, ID_LOJA) VALUES (1, 'aaa', 1, 1, 1999, 190, 1)")
conn.commit()