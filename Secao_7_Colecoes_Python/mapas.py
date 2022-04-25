"""

Mapas -> Conhecidos em Python como Dicionários.

Dicionários em Python são representados por chaves {}

# Iterar sobre dicionário

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave}: Recebi R${receita[chave]}')

# Acessando as Chaves.

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários.

print(receita.items())


for chave, valor in receita.items():
    print(f'chave= {chave} e valor= {valor}')

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Soma*, Valor Máximo*, Valor Mínimos*, Tamnho.

#* Se os valore forem todos inteiros ou reais.

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))



