import sqlite3

DB = "concessionaria.db"

def id_tipo():
    ids = []
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM TIPO")
    
    for item in cursor.fetchall():
        ids.append(item)
        
    return ids
                
                
def id_montadora():
    ids = []
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM MONTADORA")
    
    for item in cursor.fetchall():
        ids.append(item)
        
    return ids


def id_loja():
    ids = []
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM loja")
    
    for item in cursor.fetchall():
        ids.append(item)
        
    return ids