"""
    Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. Osort()
só funciona em listas.txt

Podemos utilizar o sorte() com qualquer iterável.

Como o próprio nome dis, sorted() serve para ordenar.

OBS: O sored, SEMPRE retorna uma Lista com os elementos do iterável ordenados.

"""

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)

print('######################################################')
# Teste
print('Teste')
num1 = [3, 7, 9, 5, 1 , 10, 4, 6, 8]

num2 = sorted(num1)

print(num1)
print(num2)
print('######################################################')

# Adicionando parâmetros ao sorted()
print(sorted(num1, reverse=True)) # Ordena do maior para o menor
print('######################################################')

# Podemos utilizar o sorted() para coisas mais complexas.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu Gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)
# Ordenando pelo username  - Oredem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
# Ordenando pelo username - Ordem Alfabética Inversa
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))
#  Ordenando pelo número de tweets.
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

print('######################################################\n')

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Toto", "tocou": 4},
    {"titulo": "Lady Gaga", "tocou": 9},
    {"titulo": "Michael Jackson", "tocou": 13}
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))