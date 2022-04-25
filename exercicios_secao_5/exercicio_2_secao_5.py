# 2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o número é invalido.
from math import sqrt

num = int(input('Digite um numero:'))


def raiz(num):

    if num > 0:
        raiz_a = num ** 0.5
        raiz_b = sqrt(num)

        print('A Raiz Quadrada do Número Digitado é:', raiz_a)
        print('A Raiz Quadrada do Número Digitado é:', raiz_b)
    else:
        print('O Número Digitado é Invalido')

    return 0

raiz(num)