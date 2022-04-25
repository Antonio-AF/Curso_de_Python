# 3 - Leia um número real. Se o número for positivo imprima a raiz quadrada.
# Do contrário imprima o número ao quadrado.

num = int(input('Digite um Número:'))

if num > 0:
    raiz = num ** 0.5
    print('A Raiz Quadrada do Número Digitado é:', raiz)
else:
    print('O Número Digitado ao Quadrado é: ', num**2)
