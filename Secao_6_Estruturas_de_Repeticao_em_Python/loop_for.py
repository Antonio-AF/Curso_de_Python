"""
Estrutura de Repetiçãa.

loop For.

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i++){
    //execução do loop

}

# Em Python temos:

for item in interavel:
    //execção do loop

utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:

- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma Sting)

for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)

for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterand sobre um Range)

for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])


for indice, letra in enumerate(nome):
    print(letra)

Obs: Quando não pecisamos de um valor, podemos descartá-lo utlizando m nderline (_)

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor[0])

qtd = int(input('Quantas Vezes esse loop deve rodar?' ))
soma = 0

for n in range(1, qtd):
    num = int(input(f'Imforme o {n}/ {qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


nome = 'Geek University'

for letra in nome:
    print(letra, end= '')
"""

# Original U+1F60D.

# Modificado U0001F60D.

# emoji = 'U0001F60D'

for num in range(1, 101):
    print('\U0001F60D' * num)
