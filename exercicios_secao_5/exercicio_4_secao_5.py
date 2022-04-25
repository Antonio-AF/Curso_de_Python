# 4 - Faça uma programa que leia um número e, caso ele seja positivo,
# calcule e mostre:

# > O número digitado ao quadrado
# > A raiz quadrada do número

num = int(input('Digite um número: '))

if num >= 1:
    print(f'O quadrado do número digitado {num ** 2} e a Raiz Quadrada {num ** 0.5}')

else:
    print('O número digitado não é valido')

