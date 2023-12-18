from functions.create import createDB, createTable, createTables
from functions.menu import menu, listar_ids_tipo, listar_ids_montadora, listar_ids_loja
from functions.tipo_functions import inserir_tipo
from functions.get_ids import id_tipo, id_loja, id_montadora

createTables()

# inserir_tipo('Motocicleta', 2, 2)

# print(id_tipo())

while (True):
    option = menu()
    if (option[0] == 1 and option[1] == 1):
        print("Adicionar veículo")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        ano = int(input("Ano"))
        potencia = int(input("Potencia: "))
        print()
        listar_ids_tipo(id_tipo())
        id_tipo = int(input("Tipo: "))
        listar_ids_montadora(id_montadora())
        id_montadora = int(input("Montadora: "))
        listar_ids_loja(id_loja())
        id_loja = int(input("Loja: "))

