# O que é Escopo de Variável Python?

"""  1- O Escopo de Variáveis em Python é aquela parte do código onde as variáveis são Visíveis. """

""" Revisando a Sintaxe Python """

a = 8  # Variável Global


def func():
    b = 4  # Variável Local, só é visível dentro da função ou classe.
    print(a)
    print(b)


# print(b)  # Ao tentar acessar a variável com escopo local temos um 'NameError: name 'b' is not defined'

func()

# Tipos de Escopo de Variáveis Python

""" 2 -  Existem 4 Tipos de Escopo de Variável em Python, vamos  ver uma a uma."""

# 1 - Variável de Escopo Local

'''
Acima temos o código da função func() onde foi definida a variável  (b) ao tentar acessar essa variável 
fora do escopo local dela teremos um NameError: name 'b' is not defined.
'''

# 2 - Variável de Escopo Global

''' 
No código acima temos a variável (a) que foi definida fora da função func(), essa variável tem o
Escopo Global, podendo ser acessada de qualquer lugar do código.
'''

# 3 - Variável de Escopo Enclosing (Delimitador)

''' Vejamos o Exemplo Abaixo: '''


def red():
    a = 1

    def blue():
        b = 2
        print(b)
        print(a)
    blue()
    print(a)


red()

# 4 - Variável de Escopo Incorporador

'''
    Finalmente, falamos sobre o mais amplo escopo. O escopo embutido tem todos os nomes que
são carregados em escopo variável python quando iniciamos o intérprete.
    Por exemplo, nunca precisamos importar qualquer módulo para acessar funções como
impressão() e id().
'''