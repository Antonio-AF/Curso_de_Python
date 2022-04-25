# 12 - Ler um número interio. Se o número lido for negativo, escreva a mensagem "Número inválido"
# Se o número for positivo, calcular o logaritmo deste numero.

import math


logaritmo = int(input('Digite um número para fazer o Logaritmo: '))
base = int(input('Digite a base do logaritmo'))

if logaritmo > 0:
    log = math.log(logaritmo, base)
    print(f'O logaritmo de {logaritmo} na base {base} é', log)
else:
    print('O Número Digitado é Inválido: ')