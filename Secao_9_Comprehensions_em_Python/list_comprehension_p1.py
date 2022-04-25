'''
        ###LIST COMPREHENSION###

- Utilizando List Comprehesion nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[dado for dado in iterável]


# Exemplos

numero = [1, 2, 3, 5]

res =[numero * 10 for numero in numero]

print(res)

# Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
    #- A primeira parte: for numero in numero
    #- A segunda parte: numero * 10


res = [numero / 2 for numero in numero]

print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numero]

print(res)


# List Comprehension versos Loop

# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension

print([numero * 2 for numero in numeros])
'''

# Ex. 1

nome = 'Geek University'

print([letra.upper() for letra in nome])


# Ex. 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# Ex. 3

print([numero * 3 for numero in range(1, 10)])

# Ex. 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Ex. 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
