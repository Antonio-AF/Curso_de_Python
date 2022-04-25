# 7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.

# C = 5.0*(F-32.00)/9.00

graus = float(input('Digite a Temperatura:'))

celsius = float((5.00*(graus-32))/9.00)

print("A temperatura", graus, "Fehrenheir em Celsius é:", celsius)

