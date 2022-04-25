# 43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

# * O total a pagar com desconto de 10%.
# * O valor de cada parcela, no parcelamento de 3x sem juros;
# * A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
# * A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

preco = float(input('Digite o valor da mercadoria: '))

desconto = float((preco * 10)/100)

parcela = int(input('Digite em quantas vezes quer parcelar maximo 3x: '))

if parcela == 1:

    preco = float(preco - desconto)
    comissao = float((preco * 5)/100)
    print('A comissão será de: R$', comissao)
    print('O valor Total com desconto é: R$', preco)

else:

    comissao = float((preco * 5) / 100)
    preco = float(preco / parcela)
    print('A comissão será de: R$', comissao)
    print('O valor de cada parcela é: R$', preco)
