from functions.get_ids import id_tipo, id_montadora, id_loja

def menu():
    print("Insira a operação desejada:")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Editar")
    print("4 - Listar")
    function = int(input(">>> "))
    
    print("\n1 - Veículo")
    print("2 - Loja")
    print("3 - Montadora")
    print("4 - Tipo")
    table = int(input(">>> "))
    
    if (function not in (1, 2, 3, 4)):
        function = menu()[0] 
    if (table not in (1, 2, 3, 4)):
        print("Tabela não identificada.")
        table = menu()[1]
    return [function, table]
    
    
def listar_ids_tipo(ids):
    tipos = id_tipo()
    for item in tipos:
        print(f"{item[0]} - {item[1]}")
    
def listar_ids_montadora(ids):
    tipos = id_montadora()
    for item in tipos:
        print(f"{item[0]} - {item[1]}, {item[2]}")
    
    
def listar_ids_loja(ids):
    tipos = id_montadora()
    for item in tipos:
        print(f"{item[0]} - {item[1]}, {item[2]}, {item[3]}, {item[4]}, {item[5]}")
    