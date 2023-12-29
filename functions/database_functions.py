import sqlite3
from functions.menu import listar_ids_loja

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
    
def listarVeiculos(databaseName):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM veiculo')
    for item in cursor.fetchall():
        print(f'[{item[1]}] {item[3]} {item[2]} {item[6]}')
    conn.commit()
    conn.close()
    
def listarLojas(databaseName):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM loja')
    for item in cursor.fetchall():
        print(f'{item[1]}, {item[2]}, {item[3]}, {item[4]} - {item[5]}')
    conn.commit()
    conn.close()
    
def listarMontadoras(databaseName):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM montadora')
    for item in cursor.fetchall():
        print(f'{item[1]} - {item[2]}')
    conn.commit()
    conn.close()
    
def listarTipos(databaseName):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM tipo')
    for item in cursor.fetchall():
        print(f'{item[1]}: {item[3]} passageiros, {item[2]} rodas')
    conn.commit()
    conn.close()
    
    
def listarJoinLoja(databaseName, firstTableName, secondTableName, firstTableField, secondTableField, idLoja):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {firstTableName} INNER JOIN {secondTableName} ON {firstTableField} = {secondTableField} WHERE {secondTableField} = {idLoja}')
    for item in cursor.fetchall():
        print(f"[{item[1]}] {item[3]} {item[2]} {item[6]} : {item[10]}, {item[11]}, {item[12]}, {item[13]}, {item[14]}")
        
def listarJoinMontadora(databaseName, firstTableName, secondTableName, firstTableField, secondTableField, idMontadora):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    

    cursor.execute(f'SELECT * FROM {firstTableName} INNER JOIN {secondTableName} ON {firstTableField} = {secondTableField} WHERE {secondTableField} = {idMontadora}')
    for item in cursor.fetchall():
        print(f"[{item[1]}] {item[3]} {item[2]} {item[6]} : {item[10]}, {item[11]}")
        
def listarJoinTipo(databaseName, firstTableName, secondTableName, firstTableField, secondTableField):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {firstTableName} INNER JOIN {secondTableName} ON {firstTableField} = {secondTableField}')
    for item in cursor.fetchall():
        print(f"[{item[1]}] {item[3]} {item[2]} {item[6]} : {item[10]}, {item[11]} rodas, {item[12]} passageiros")
        
def atualizarVeiculo(databaseName, tableName, field, value, idField, objectID):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {tableName} SET {field} = "{value}" WHERE {idField} = {objectID}')
    conn.commit()
    