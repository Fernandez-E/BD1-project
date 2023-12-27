from functions.get_ids import get_ids

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
    
    
def listar_ids_tipo():
    tipos = get_ids('tipo')
    for item in tipos:
        print(f"{item[0]} - {item[1]}")
    
def listar_ids_montadora():
    tipos = get_ids('montadora')
    for item in tipos:
        print(f"{item[0]} - {item[1]}, {item[2]}")
    
    
def listar_ids_loja():
    tipos = get_ids('loja')
    for item in tipos:
        print(f"{item[0]} - {item[1]}, {item[2]}, {item[3]}, {item[4]}, {item[5]}")
        

def listar_ids_veiculos():
    veiculos = get_ids('veiculo')
    for veiculo in veiculos:
        print(f'{veiculo[0]} - Placa: {veiculo[1]} >>> {veiculo[3]}, {veiculo[2]}, {veiculo[6]}')

def listar_veiculos():
        print("Quais veículos deseja listar?")
        print("1 - Todos")
        print("2 - Por loja")
        print("3 - Por montadora")
        print("4 - Por tipo")

        
        veiculos = int(input(">>> "))
        if (veiculos not in (1, 2, 3, 4)):
            veiculos = listar_veiculos()
        return veiculos