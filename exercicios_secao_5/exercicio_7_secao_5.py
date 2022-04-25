# 7 - Faça um programa que receba dois npumero e mostre o maior. Se por acaso,
# os dois forem iguais, imprima a mensagem Números iguais.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))

if num1 > num2:
    print(f'O numero {num1} é mairo que o {num2}')

elif num1 == num2:
    print(f'Os numeros digitados são Iguais')

else:
    print(f'O numero {num2} é maior que o {num1}')

