from functions.create import createDB, createTable, createTables
from functions.menu import menu, listar_veiculos, listar_ids_tipo, listar_ids_montadora, listar_ids_loja, listar_ids_veiculos
from functions.tipo_functions import inserir_tipo
from functions.get_ids import get_ids
from functions.database_functions import atualizarVeiculo, inserir, remover, listarVeiculos, listarLojas, listarMontadoras, listarTipos, listarJoinLoja, listarJoinMontadora, listarJoinTipo

createTables()

# inserir_tipo('Motocicleta', 2, 2)

# print(id_tipo())

DB = 'concessionaria.db'

while (True):
    option = menu()
    if (option[0] == 1 and option[1] == 1): # ADICIONAR VEÍCULO
        TABLE = 'veiculo'
        print("Adicionar veículo")
        rua = input("Placa: ")
        numero = input("Modelo: ")
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
        values = f'"{rua}", "{cor}", "{numero}", {id_tipo}, {id_montadora}, {ano}, {potencia}, {id_loja}'
        
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
        TB = 'veiculo'
        TB_NAME = 'id_veiculo'
        id_remover = int(input("Id do veículo para remover: "))
        remover(DB, TB, TB_NAME, id_remover)
    elif (option[0] == 2 and option[1] == 2): # REMOVER LOJA
        listar_ids_loja()
        TB = 'loja'
        TB_NAME = 'id_loja'
        id_remover = int(input("Id da loja para remover: "))
        remover(DB, TB, TB_NAME, id_remover)    
    elif (option[0] == 2 and option[1] == 3): # REMOVER MONTADORA
        listar_ids_montadora()
        TB = 'montadora'
        TB_NAME = 'id_montadora'
        id_remover = int(input("Id da montadora para remover: "))
        remover(DB, TB, TB_NAME, id_remover)
    elif (option[0] == 2 and option[1] == 4): # REMOVER TIPO
        listar_ids_tipo()
        TB = 'tipo'
        TB_NAME = 'id_tipo'
        id_remover = int(input("Id do tipo de veículo para remover: "))
        remover(DB, TB, TB_NAME, id_remover)

    elif (option[0] == 3 and option[1] == 1): # TODO: EDITAR VEÍCULO
        print("Qual veículo deseja modificar?")
        listar_ids_veiculos()
        mod = int(input(">>> "))
        
        print("O que deseja modificar?")
        print("1 - Placa")
        print("2 - Modelo")
        print("3 - Cor")
        print("4 - Ano")
        print("5 - Potencia")
        field = int(input(">>> "))
        
        if field == 1:
            rua = input("Nova placa: ")
            atualizarVeiculo(DB, 'veiculo', "placa", rua, "id_veiculo", mod)
        elif field == 2:
            numero = input("Novo modelo: ")
            atualizarVeiculo(DB, 'veiculo', "modelo", numero, "id_veiculo", mod)
        elif field == 3:
            cor = input("Nova Cor: ")
            atualizarVeiculo(DB, 'veiculo', "cor", cor, "id_veiculo", mod)
        elif field == 4:
            ano = int(input("Novo ano: "))
            atualizarVeiculo(DB, 'veiculo', "ano", ano, "id_veiculo", mod)
        elif field == 5:
            ano = int(input("Nova potencia: "))
            atualizarVeiculo(DB, 'veiculo', "potencia", potencia, "id_veiculo", mod)
            
          
    elif (option[0] == 3 and option[1] == 2): # TODO: EDITAR LOJA
        print("Qual loja deseja modificar?")
        listar_ids_loja()
        mod = int(input(">>> "))
        
        print("O que deseja modificar?")
        print("1 - Rua")
        print("2 - Numero")
        print("3 - Bairro")
        print("4 - Cidade")
        print("5 - Estado")
        field = int(input(">>> "))
        
        if field == 1:
            rua = input("Nova rua: ")
            atualizarVeiculo(DB, 'loja', "rua_loja", rua, "id_loja", mod)
        elif field == 2:
            numero = input("Novo número: ")
            atualizarVeiculo(DB, 'loja', "numero_loja", numero, "id_loja", mod)
        elif field == 3:
            bairro = input("Novo bairro: ")
            atualizarVeiculo(DB, 'loja', "bairro_loja", bairro, "id_loja", mod)
        elif field == 4:
            cidade = int(input("Nova cidade: "))
            atualizarVeiculo(DB, 'loja', "cidade_loja", cidade, "id_loja", mod)
        elif field == 5:
            estado = int(input("Novo estado: "))
            atualizarVeiculo(DB, 'loja', "estado_loja", estado, "id_loja", mod)
    elif (option[0] == 3 and option[1] == 3): # TODO: EDITAR MONTADORA
        print("Qual montadora deseja modificar?")
        listar_ids_montadora()
        mod = int(input(">>> "))
        
        print("O que deseja modificar?")
        print("1 - Nome")
        print("2 - Nacionalidade")
        field = int(input(">>> "))
        
        if field == 1:
            nome = input("Novo nome: ")
            atualizarVeiculo(DB, 'montadora', "nome_montadora", nome, "id_montadora", mod)
        elif field == 2:
            nacionalidade = input("Nova nacionalidade: ")
            atualizarVeiculo(DB, 'montadora', "nacionalidade", nacionalidade, "id_montadora", mod)

    elif (option[0] == 3 and option[1] == 4): # TODO: EDITAR TIPO
        print("Qual tipo de veículo deseja modificar?")
        listar_ids_tipo()
        mod = int(input(">>> "))
        
        print("O que deseja modificar?")
        print("1 - Nome")
        print("2 - Quantidade de rodas")
        print("2 - Quantidade de passageiros")        
        field = int(input(">>> "))
        
        if field == 1:
            nome = input("Novo nome: ")
            atualizarVeiculo(DB, 'tipo', "tipo", nome, "id_tipo", mod)
        elif field == 2:
            rodas = input("Nova quantidade de rodas: ")
            atualizarVeiculo(DB, 'tipo', "quantidade_rodas", rodas, "id_tipo", mod)
        elif field == 3:
            passageiros = input("Nova quantidade de passageiros: ")
            atualizarVeiculo(DB, 'tipo', "quantidade_passageiros", passageiros, "id_tipo", mod)
                       
    elif (option[0] == 4 and option[1] == 1): # TODO: LISTAR VEÍCULO
        join = listar_veiculos() 
        if join == 1:
            listarVeiculos(DB)
        elif (join == 2): # TODO: LISTAR LOJA
            listar_ids_loja()
            idLoja = int(input('>>> '))
            listarJoinLoja(DB, 'veiculo', 'loja', 'veiculo.id_loja', 'loja.id_loja', idLoja)
        elif (join == 3): # TODO: LISTAR MONTADORA
            listarJoinMontadora(DB, 'veiculo', 'montadora', 'veiculo.id_montadora', 'montadora.id_montadora')
        elif (join == 4): # TODO: LISTAR TIPO
            listarJoinTipo(DB, 'veiculo', 'tipo', 'veiculo.id_tipo', 'tipo.id_tipo') 
    elif (option[0] == 4 and option[1] == 2): # TODO: LISTAR LOJAS
        listarLojas(DB)
    elif (option[0] == 4 and option[1] == 3): # TODO: LISTAR MONTADORAS
        listarMontadoras(DB)
    elif (option[0] == 4 and option[1] == 4): # TODO: LISTAR TIPOS
        listarTipos(DB)
