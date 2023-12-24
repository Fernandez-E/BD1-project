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
    
def listar(databaseName, tableName):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {tableName}')
    for item in cursor.fetchall():
        ...
    conn.commit()
    conn.close()
    
def listarJoin(databaseName, firstTableName, secondTableName, firstTableField, secondTableField):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {firstTableName} INNER JOIN {secondTableName} ON {firstTableField} = {secondTableField}')
    for item in cursor.fetchall():
        print(f"[{item[1]}] {item[3]} {item[2]} {item[6]} : {item[10]}, {item[11]}, {item[12]}, {item[13]}, {item[14]}")