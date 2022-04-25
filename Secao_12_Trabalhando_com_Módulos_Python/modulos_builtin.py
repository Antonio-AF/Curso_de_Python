"""
Trabalhando com Módulos Builtin ( módulos integrados, que já vem instalados no Python)

|Python|Módulos builtin|


# https://docs.python.org/3/py-modindex.html

# Utilizando alias (apelidos) para modulos/função

import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando o (*)

from random import *
# import random

print(random())


# Importando todo o módulo

import random

print(random.random())


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

"""

# Costumamos a utilizar tuple para colocar mútiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice

)

print(random())
print(randint(45, 899))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))