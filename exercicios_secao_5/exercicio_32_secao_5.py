"""
    32 - Escreva um programa que leia o código do produto escolhido do cardápio de uma lanchonete
    e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução
    somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:

"""


cachorro_Quente = 100
bauru_Simples = 101
bauru_Com_Ovo = 102
hamburguer = 103
cheeseburguer = 104
suco = 105
refrigerante = 106

print('\n')
print('Cardápio da Lanchonete Day_of_Day\n')
print(f'{cachorro_Quente} - Cahorro Quente')
print(f'{bauru_Simples} - Bauru Simples')
print(f'{bauru_Com_Ovo} - Bauru com Ovo')
print(f'{hamburguer} - Hamburguer')
print(f'{cheeseburguer} - Cheeseburguer')
print(f'{suco} - Suco')
print(f'{refrigerante} - Refrigerante\n')

item = int(input('Digite o código do produto solictado: '))
qtda = int(input('Digite a quantidade: '))


def conta(item, qtda):

    if item == 100 or item == 103:
        nota = float(qtda * 1.20)

    elif item == 101:
        nota = float(qtda * 1.30)

    elif item == 102:
        nota = float(qtda * 1.50)

    elif item == 104:
        nota = float(qtda * 1.70)

    elif item == 105:
        nota = float(qtda * 2.20)

    elif item == 106:
        nota = float(qtda * 1.00)

    return nota


print(f'O valor Total do Pedido é R${conta(item, qtda)}')
