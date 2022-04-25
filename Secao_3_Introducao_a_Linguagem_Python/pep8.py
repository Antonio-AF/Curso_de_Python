"""
PEP8 - Python Enhacement Proposal:

    São proposta de melhrorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrver  códigos Python de forma Pythônica.
###########################################################
[1] - Utilize Camel Case para nomes de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


###########################################################
[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;


def soma():
    pass

def soma_dois():
    pass
###########################################################
[3] - Utilize 4 espaços para identação! (Não utilizar o tab)


if 'a' in 'banana':
    print('tem)
###########################################################
[4] - Linas em branco

class Classe:
    pass


class ClasseSoma:
    pass
############################################################
[5] - Iports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado.

import sys, os

#  Importt Certo.

import sys
import os

# Não há problema em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, remenda-se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados notopo do arquiv, logo depois de quaisquer comentário ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções.

# Não faça:

funcao( algo[ 1 ], {outro: 2} ]

# Faça:

funcao(algo[1], {outro: 2}

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não Faça:

x            =1
y            =3
variavel_long=5

[7] - Temine sempre uma instrução com uma nova linha.
"""


import this


