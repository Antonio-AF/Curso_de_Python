"""
        ### Utilizando Lambdas ###

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja
funções anônimas.

# Função em Python

def soma(a, b):
    return a + b

# Uma simples função em Python.

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(5))

#Expressão Lambda

lambda x: 3 * x + 1

# Como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1

print(calc(9))
print(calc(2))


# Podemos ter expressões lambdas com múltiplas  entradas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' antonio', 'Amaral '))
print(nome_completo(' antonio ', 'Amaral Farias'))


# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também

amar = lambda: 'Como não amar Python '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1/ x + 1 / y + 1 / z)

# n = lambda x1, x1, . . ., xn: <expressão>

print(amar())
print(uma(5))
print(duas(5, 7))
print(tres(3, 5, 9))

#OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError.

# Outro exemplo

autores = ['Isac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""


# Função Quadratica

#f(x) = a * x**2 + b*x + c

# Definindo a Função.

def feradora_funcao_quadratica(a, b, c):
    '''Retorna a função f(x)=a*x**2+b*x+c'''
    return lambda x: a * x ** 2 + b * x + c

teste = feradora_funcao_quadratica(2, 3 , -5)

print(teste(0))
print(teste(1))
print(teste(58))