# 9 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.

# K = C + 273.15.

graus = float(input('Digite a temperatura: '))

kelvin = float(graus + 273.15)

print('A temperatura de', graus, 'K, em graus Celsius é:', kelvin, 'C°')
