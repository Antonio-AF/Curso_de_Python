"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Pecisamos conhecer o range para trabalhar melhor com loop for.

Ranges são tilizados paa gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1.
ranges(valor_de_parada)

Obs: valor_de_parada não inclusive (inicio padrão , e passo de 1 em 1)

# Exemplo Forma 1

for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

Obs: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(4, 11):
    print(num)

# Foma 3

range(valor_de_inicio, valor_de_parada, passo)

Obs: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuáio)

# Exemplo Forma 3

for num in range(5, 50, 5):
    print(num)


# Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

Obs: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuáio)


"""
# Exemplo Forma 4

for num in range(10, 0, -1 ):
    print(num)
