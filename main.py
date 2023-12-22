from functions.create import createDB, createTable, createTables
from functions.menu import menu, listar_ids_tipo, listar_ids_montadora, listar_ids_loja, listar_ids_veiculos
from functions.tipo_functions import inserir_tipo
from functions.get_ids import get_ids
from functions.database_functions import inserir

createTables()

# inserir_tipo('Motocicleta', 2, 2)

# print(id_tipo())

DB = 'concessionaria.db'

while (True):
    option = menu()
    if (option[0] == 1 and option[1] == 1): # ADICIONAR VEÍCULO
        TABLE = 'veiculo'
        print("Adicionar veículo")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        ano = int(input("Ano: "))
        potencia = int(input("Potencia: "))
        print()
        listar_ids_tipo()
        id_tipo = int(input("Tipo: "))
        listar_ids_montadora()
        id_montadora = int(input("Montadora: "))
        listar_ids_loja()
        id_loja = int(input("Loja: "))
        
        columns = 'PLACA, COR, MODELO, ID_TIPO, ID_MONTADORA, ANO, POTENCIA, ID_LOJA'
        values = f'"{placa}", "{cor}", "{modelo}", {id_tipo}, {id_montadora}, {ano}, {potencia}, {id_loja}'
        
        inserir(DB, TABLE, columns, values)
    elif (option[0] == 1 and option[1] == 2): # ADICIONAR LOJA
        print("Adicionar loja")
        table = 'loja'
        rua = input("Logradouro: ")
        numero = int(input("Número: "))
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        columns = 'RUA_LOJA, NUMERO_LOJA, BAIRRO_LOJA, CIDADE_LOJA, ESTADO_LOJA'
        values = f'"{rua}", {numero}, "{bairro}", "{cidade}", "{estado}"'
        inserir(DB, table, columns, values)
    elif (option[0] == 1 and option[1] == 3): # ADICIONAR MONTADORA
        print("Adicionar Montadora")
        table = 'montadora'
        nome = input("Nome da montadora: ")
        nacionalidade = input("Nacionalidade da montadora: ")

        columns = 'NOME_MONTADORA, NACIONALIDADE'
        values = f'"{nome}", "{nacionalidade}"'
        inserir(DB, table, columns, values)
    elif (option[0] == 1 and option[1] == 4): # ADICIONAR TIPO
        print("Adicionar Tipo")
        table = 'tipo'
        tipo = input("Tipo de veículo: ")
        passageiros = int(input("Quantidade de passageiros: "))
        rodas = int(input("Quantidade de rodas: "))
        columns = 'TIPO, QUANTIDADE_RODAS, QUANTIDADE_PASSAGEIROS'
        values = f'"{tipo}","{rodas}", "{passageiros}"'
        inserir(DB, table, columns, values)
        
    elif (option[0] == 2 and option[1] == 1): # REMOVER VEÍCULO
        listar_ids_veiculos()
        
    elif (option[0] == 2 and option[1] == 2): # REMOVER LOJA
        ...
    elif (option[0] == 2 and option[1] == 3): # REMOVER MONTADORA
        ...
    elif (option[0] == 2 and option[1] == 4): # REMOVER TIPO
        ...

    elif (option[0] == 3 and option[1] == 1): # EDITAR VEÍCULO
        ...       
    elif (option[0] == 3 and option[1] == 2): # EDITAR LOJA
        ...
    elif (option[0] == 3 and option[1] == 3): # EDITAR MONTADORA
        ...
    elif (option[0] == 3 and option[1] == 4): # EDITAR TIPO
        ...
        
    elif (option[0] == 4 and option[1] == 1): # LISTAR VEÍCULO
        ...       
    elif (option[0] == 4 and option[1] == 2): # LISTAR LOJA
        ...
    elif (option[0] == 4 and option[1] == 3): # LISTAR MONTADORA
        ...
    elif (option[0] == 4 and option[1] == 4): # LISTAR TIPO
        ...
