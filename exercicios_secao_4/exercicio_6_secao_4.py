#  6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.

# F = C*(9.0/5.0)+32.0

celsius = float(input('Digite a Temperatura:'))

fahrenheit = float(celsius*(9/5))+32

print('A temperatura', celsius, 'Em Fahrenheit é: ', fahrenheit)
