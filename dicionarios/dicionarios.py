# > DICIONÁRIOS

# Criando dicionários


dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Anderson', 'idade': 41, 'altura': 1.77 }

print(dicionario)
print(dicionario['idade'])


# Adicionar elementos em dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)


# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)