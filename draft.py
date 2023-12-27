from functions.database_functions import listarJoin

DB = 'concessionaria.db'
listarJoin(DB, 'veiculo', 'loja', 'veiculo.id_loja', 'loja.id_loja')