# 19 - Leia um valor de colume em litros e apresente-o convertido em metros cúbicos m³.

# M = L/1000.

litros = float(input('Digite quantos litros você quer converter em m³: '))

volume  = float(litros/1000)

print('A quantidade de', litros, 'convertida é de:', volume,'m³')
