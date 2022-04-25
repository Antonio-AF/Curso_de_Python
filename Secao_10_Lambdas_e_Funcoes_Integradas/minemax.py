"""
        Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

#Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

print('#############################################################################')

print(max(4, 8, 78, 89))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek University'))

print('#############################################################################')

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.

#Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

print('#############################################################################')

print(min(4, 8, 78, 89))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University'))

print('#############################################################################')

"""

# outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key= lambda nome: len(nome)))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Toto", "tocou": 4},
    {"titulo": "Lady Gaga", "tocou": 9},
    {"titulo": "Michael Jackson", "tocou": 13}
]

print(max(musicas, key =lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key =lambda musica: musica['tocou'])['titulo'])