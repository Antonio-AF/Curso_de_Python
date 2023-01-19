"""

Entendendo Iterators e Iterables

Iterator  _>
    - Um objeto que pode ser iterado.
    - Um Objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable ->
    - Um objeto que irpa retornar um iterator quando a função iter() for chamada.

"""

nome = "Antonio" # É um iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6] # É um terable mas não pe um iterator.

iter1 = iter(nome)
iter2 = iter(numeros)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))


print(next(iter2))




# print(next(nome)) # Gera um -> TypeError: 'str' object is not an iterator

# print(next(numeros)) # Gera um -> TypeError: 'list' object is not an iterator

for letra in nome:
    print(f'{letra}')


# Conteúdo Extra:

"""
    Iteradores do Python
    
    Um iterador é um objeto que contém um número contável de valores.

    Um iterador é um objeto que pode ser iterado, o que significa que você pode percorrer todos os valores.

    Tecnicamente, em Python, um iterador é um objeto que implementa o protocolo do iterador, que consiste nos métodos __iter__() e __next__().

"""

"""
    Iterador vs Iterável
    Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. Eles são contêineres iteráveis ​​dos quais você pode obter um iterador.

    Todos esses objetos possuem um iter()método que é usado para obter um iterador:

"""