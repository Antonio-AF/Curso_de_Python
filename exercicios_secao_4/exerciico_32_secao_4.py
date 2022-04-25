# 32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

num = int(input('Digite um numero Inteiro: '))

triplo = num * 3
sucessor = triplo + 1

dobro = num * 2
antecessor = dobro - 1

print('A soma é: ', sucessor + antecessor)
