"""
            ### REDUCE ###

OBS: A partir do Python 3+ a função reduce() não é mais uma função integrada  (buit-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Ulize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for e mais legível.

Para entender o reduce()

# Imagine se você tem uma coleção de Dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parâmentros:

def funcao(x, y)
    return x * y

Assim como a função map() e filter(), a função reduce() recebe dois parâmetros: a funão e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros  elementos da coleção e guarda o resultado.
    Passo 2: res = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3 : res3 = f(res2, a4)
    .:cvar.
    .:cvarPasso n: resn  = f(resn, an)
Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final
redude() irá retornar o resultdo final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)


"""
# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplcar todos os números de uma lista.

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)