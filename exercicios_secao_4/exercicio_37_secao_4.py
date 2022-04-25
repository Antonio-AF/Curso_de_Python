# 38 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.

preco = float(input('Digite o Valor do Produto: '))

desconto = float(preco - ((preco * 12)/100))

print('O valor a ser pago com desconto é: ', desconto)
