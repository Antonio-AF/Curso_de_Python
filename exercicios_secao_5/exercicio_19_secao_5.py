"""
    19 - Faça um programa para se um determinado número inteiro é divisível por 3 ou
    5, mas não simultaneamente pelo dois.
"""

num = int(input('Digite um número inteiro: '))


def div_por(num):
    if num % 3 == 0 and num % 5 == 0:
        print('O numero digitado é divisivel por 3 e 5 digite outro nunero')
    elif num % 3 == 0:
        print('O número só é divisivel por 3!!!')
    elif num % 5 == 0:
        print('O numero só é divisivel por 5!!!')
    else:
        print('numero invalido')

    return "O número digitado foi ", num

print(div_por(num))