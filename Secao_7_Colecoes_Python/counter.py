"""
Módulos Collections - Counter. (Tradução direta => contador)

Collections -> High-performance Container Datatypes

Counter -> Recebe um interável como parâmetro ecria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro
e como valor aquantidade de ocorrências desse elemento.

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui estamos usando uma lista.
lista = [1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 6, 6, 6, 45, 89, 899]

# Utilizndo o Counter.
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 4, 2: 4, 3: 4, 6: 3, 4: 2, 5: 2, 45: 1, 89: 1, 899: 1})

# Veja que, para cada elemento dalista, o Counter criou uma chave e colocou como
# valor a quantidade de ocorrências.


# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

# Realizando o import
from collections import Counter

# Exemplo 3

texto = """Mapeamento do Ecossistema de apoio ao empoderamento da mulher 
Elaboração de Material Didático para o Ensino de Data Science Aplicado a Performabilidade"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências.
print(res.most_common(5))