import sqlite3

def createDB(databaseName):
    conn = sqlite3.connect(databaseName)
    
    
def createTable(databaseName, tableName, columns):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableName} ({columns})")
    conn.close()
    
def createTables():
    DB = "concessionaria.db"
    VEICULO = "veiculo"
    COLUMNS_VEICULO = f"ID_VEICULO INTEGER PRIMARY KEY AUTOINCREMENT, PLACA VARCHAR(8) UNIQUE NOT NULL, COR VARCHAR(32), MODELO VARCHAR(64) NOT NULL, ID_TIPO INT, ID_MONTADORA INT, ANO INT NOT NULL, POTENCIA INT NOT NULL, ID_LOJA INT, FOREIGN KEY(ID_TIPO) REFERENCES TIPO(ID_TIPO), FOREIGN KEY(ID_MONTADORA) REFERENCES MONTADORA(ID_MONTADORA), FOREIGN KEY(ID_LOJA) REFERENCES LOJA(ID_LOJA)"
    TIPO = "tipo"
    COLUMNS_TIPO  = f"ID_TIPO INTEGER PRIMARY KEY AUTOINCREMENT, TIPO VARCHAR(32) NOT NULL, QUANTIDADE_RODAS INT NOT NULL, QUANTIDADE_PASSAGEIROS INT NOT NULL"
    MONTADORA = "montadora"
    COLUMNS_MONTADORA = f'ID_MONTADORA INTEGER PRIMARY KEY AUTOINCREMENT, NOME_MONTADORA VARCHAR(32) NOT NULL, NACIONALIDADE VARCHAR(32) NOT NULL'
    LOJA = "loja"
    COLUMNS_LOJA = f'ID_LOJA INTEGER PRIMARY KEY AUTOINCREMENT, RUA_LOJA VARCHAR(128) NOT NULL, NUMERO_LOJA INTEGER NOT NULL, BAIRRO_LOJA VARCHAR(64) NOT NULL, CIDADE_LOJA VARCHAR(64) NOT NULL, ESTADO_LOJA VARCHAR(32) NOT NULL'

    createDB(DB)
    createTable(DB, TIPO, COLUMNS_TIPO)
    createTable(DB, MONTADORA, COLUMNS_MONTADORA)
    createTable(DB, LOJA, COLUMNS_LOJA)
    createTable(DB, VEICULO, COLUMNS_VEICULO)