# 35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz de a² + b².
# Faça um programa que recebe os valores de a e b e calcule o valor da hipotenusa através da equação.
# Imprima o resultado da operação.

a = int(input('Digite o valor de A: '))
b = int(input("Digite o valor de B: "))

hip = float((a ** 2 + b ** 2) ** 0.5)

print(f"A Hipotenusa do triângulo de Catetos {a, b} é:", hip)
