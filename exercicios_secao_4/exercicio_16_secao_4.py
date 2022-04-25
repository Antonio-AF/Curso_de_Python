# 16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.

# C = P * 2.54

"""
C é o comprimento em centímetros
P é o comprimento em polegadas.

"""
comprimento = float(input('Digite um comprimento em Polegadas:'))

centimetros = comprimento * 2.54

print("O comprimento convertido para Centimetros é %.2f:" %centimetros)

