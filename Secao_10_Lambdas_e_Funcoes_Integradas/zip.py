"""
    Zip

zip() -> Cria um iterável (Zip Object) quie agrega elemento de cada um dos interáveis passados como entrada em pares.

"""

# Exemplos

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9, 10, 11, 12]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla ou Dicionário

print(list(zip1))

print(tuple(zip1))

print(set(zip1))

print(dict(zip1))