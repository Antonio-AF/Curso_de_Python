# 6 - Escreva um programa que, dados dois números interios, mostre na tela
# o maior deles assim como a diferença existente entre ambos.

num1 = int(input('Digite um Número: '))
num2 = int(input('Digite um segundo Número: '))

if num1 > num2:
    print(f'O numero {num1} é maior que o {num2} e a diferença entre eles é '
          f'{num1 - num2}')
else:
    print(f'Onumero {num2} é maior que o {num1} e a diferença entre eles é '
          f'{num2 - num1}')

