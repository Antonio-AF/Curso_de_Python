# 17 - Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.

# P = C/2.54

comprimento = float(input('Digite um comprimento em Centimetros:'))

polegadas = float(comprimento/2.54)

print("O comprimento convertido para Polegadas é %.2f" %polegadas)
