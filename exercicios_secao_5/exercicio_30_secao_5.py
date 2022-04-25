"""
    30 - Faça um programa que receba três números e mostre-os em ordem crescente.

"""

print('Digite Três números:')
num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num3: '))

numeros = [num1, num2, num3]

numeros_ordenados = sorted(numeros)

print(numeros_ordenados)