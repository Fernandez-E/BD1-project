import sqlite3

def inserir(databaseName, tableName, columns, values):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {tableName} ({columns}) VALUES ({values}) ')
    conn.commit()
    conn.close()
    