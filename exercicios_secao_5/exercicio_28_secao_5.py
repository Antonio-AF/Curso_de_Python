"""
    28 - Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias
    de acordo com um valor numérico digitado pelo usuário:


    (a) Geométrica: (x*y*z)**1/3
    (b) Ponderada: (x + 2 * y + 3 *z)/6
    (c) Harmônica: 1/ (1/x + 1/y + 1/z)
    (d) Aritmética: x + y + z /3

"""
print('GEOMETRICA, PONDERADA, HARMONICA, ARITMETICA')
operacao = input('Digite uma das o perações listadas: ')

x = int(input('Digite um valor para X: '))
y = int(input('Digite um valor para Y: '))
z = int(input('Digite um valor para Z: '))

geometrica = float(x*y*z)**0.3333
ponderada = float((x + 2) * (y + 3) * z)/6
harmonica = float(1/(1/x + 1/y + 1/z))
aritmetica = float(x + y + z) /3

if operacao == 'GEOMETRICA':
    print(f' A média geometrica é {geometrica}')
elif operacao == 'PONDERADA':
    print(f' A média ponderada é {ponderada}')
elif operacao == 'HARMONICA':
    print(f'A média Harmonica é {harmonica}')
elif operacao == 'ARITMETICA':
    print(f' A média Aritmética é {aritmetica}')
else:
    print('ERRO')





