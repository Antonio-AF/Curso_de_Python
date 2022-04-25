# 46 - Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
#  Gere outro número formado pelos dígitos invertidos do numnero lido.


num = input('Digite um número de 100 a 999: ')


num1 = list(num[::-1])

novo1 = str(num1[0])
novo2 = str(num1[1])
novo3 = str(num1[2])

numero_novo = novo1+novo2+novo3

print('O número gerado é: ', numero_novo)


