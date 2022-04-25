comprimento = float(input('Digite o comprimento a ser convertido: '))

while True: # Para fazer o laço o parâmetro deve ser True, enquanto a condição for ele faz as conversões.

    #comprimento = float(input('Digite o comprimento a ser convertido: '))

    conversao = int(input('Digite 1 para converter em Metros ou 2 para converter em Jardas: '))

    if conversao == 1:
        metros = float(.91 * comprimento)
        print(f'Para {comprimento} Jardas Temos %.2f' % metros, 'Metros.')
        break
    elif conversao == 2:
        jardas = float(comprimento/0.91)
        print(f'Para {comprimento} Metros Temos %.2f' % jardas, 'Jardas.')
        break
    print('Digite um valor valido')
