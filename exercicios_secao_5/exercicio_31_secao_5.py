"""
    31 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a teabela
    a seguir, verifique e  mostra qua a classificação dessa pessoa.

    Altura           |                   Peso
                     |
                        Até 60  | Entre 60 e 90 (inclsive | Acima de 90
    Menor que 1,20       A              D                       G
    De 1,20 a 1,70       B              E                       H
    Maior que 1,70       C              F                       I

"""

altura = float(input('Digiete sua altura: '))
peso = int(input('Digite o seu peso: '))

if altura < 1.20:
    if peso <= 60:
        print('Você pertence a Classe A')
    elif peso > 60 and peso <= 90:
        print('Você pertence a Classe D')
    elif peso > 90:
        print('Você pertence a Classe G')
elif altura >= 1.20 and altura <= 1.70:
    if peso <= 60:
        print('Você pertence a Classe B')
    elif peso > 60 and peso <= 90:
        print('Você pertence a Classe E')
    elif peso > 90:
        print('Você pertence a Classe H')
elif altura > 1.70:
    if peso <= 60:
        print('Você pertence a Classe B')
    elif peso > 60 and peso <= 90:
        print('Você pertence a Classe E')
    elif peso > 90:
        print('Você pertence a Classe H')
else:
    print('erro')
