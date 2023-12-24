import sqlite3

def inserir(databaseName, tableName, columns, values):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {tableName} ({columns}) VALUES ({values}) ')
    conn.commit()
    conn.close()
    
    
def remover(databaseName, tableName, idFieldName, id):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {tableName} WHERE {idFieldName} = {id}')
    conn.commit()
    conn.close()