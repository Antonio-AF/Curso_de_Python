# 28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))

valor1 = num1 ** 2
print(valor1)
valor2 = num2 ** 2
print(valor2)
valor3 = num3 ** 2
print(valor3)

soma = valor1 + valor2 + valor3

print('A soma dos Quadrados dos Valores Digitados é: ', soma)
