# 8 - Leia uma temperata em graus Kelvin e apresente-a convertida em gras Celsius.

# C = k - 273.15

graus = float(input('Digite a temperatura:'))

celsius = float(graus - 273.15)

print('A temperatura', graus, 'Kelvin em Celsius é:', celsius)
