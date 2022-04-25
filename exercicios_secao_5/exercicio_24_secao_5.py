"""
    24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
    de imposto sobre o prodto (MG = 7%, SP = 12%, RJ = 15%, MS = 8%). Faça um programa em que o usuário entre com
    o valor e o estado destino do produto e o programa retorne o preço final acrescido do imposto do estado em que
    ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

"""


valorProduto = float(input('Digite o valor do Produto: '))
destino = int(input('Digite um dos estados 1 = MG, 2 = SP, 3 = RJ, 4 = MS: '))


def imposto(destino, valorProduto):
    if destino == 1:
        icms = valorProduto + (valorProduto * 0.07)
        print("O valor do Produto com Imposto é: R$",icms)
    elif destino == 2:
        icms = valorProduto + (valorProduto * 0.12)
        print("O valor do Produto com Imposto é: R$",icms)
    elif destino == 3:
        icms = valorProduto + (valorProduto * 0.15)
        print("O valor do Produto com Imposto é: R$",icms)
    elif destino == 4:
        icms = valorProduto + (valorProduto * 0.08)
        print("O valor do Produto com Imposto é: R$",icms)
    else:
        print('Erro Digite Um Estado Valido!!!')


imposto(destino, valorProduto)