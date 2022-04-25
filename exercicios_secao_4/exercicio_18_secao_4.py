# 18 - Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.

# L = 1000 * M

volume = float(input('Digite quantos m³ você quer converter para Litros: '))

litros = float(1000 * volume)

print("A quantidade de", volume,'m³ em Litros é:', litros,'l')
