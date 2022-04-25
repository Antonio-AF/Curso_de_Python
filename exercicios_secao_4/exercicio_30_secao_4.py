# 30 - Leia um valor em real e a cotação do dólar, Em seguida, imprima o valor correspondente em dólares.

valor = float(input('Digite o Valor a ser convertido em Dólares: '))

dolarhoje = float(input('Qual é a Cotação do Dólar Hoje: '))

conver  = float(valor * dolarhoje)

print(f'O valor de R${valor} em dólar é $', conver)
