"""
            ### FUNÇÂO FILTER ###

filter() -> Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6

media = sum(valores) / len(valores)

print(media)


# Biblioteca para trabalhar com dados estatisticos.

import statistics

# Dados coletados de algum sensor.
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(media)

# OBS: Assim como a função map(), a filter() recebe dois parâmentros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função ma(), após serem utilizados os dados de filter() eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

#res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)


print(list(res))


# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a funçao para
# cada elemento do iterável.

# filter() -> Recebe dois parâmentros, uma função e um iterável e retorna um objeto filtrando apenas
# os elementos de acordo com a função.


# Exemplo mais complexo.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu Gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuários que estão intivos no Twitter.
# Forma 1
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
"""
# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, dede que cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)