# 53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bom como
#o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

largura_do_terreno = int(input('Digite a Largura do Terreno: '))
comprimento_do_terreno = int(input('Digite o Comprimento do Terreno: '))

preco_cerca = float(input('Digite o preço da Tela R$'))

custo = ((largura_do_terreno * 2 + comprimento_do_terreno * 2 ) * preco_cerca)


print('O custo para cercar todo o Terreno é de R$', custo)


