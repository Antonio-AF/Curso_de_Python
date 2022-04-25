# 21 E 22 - Leia um valor de comprimento em jardas e apresente-o conertido em metros, e vice e versa.

# M = 0.91 * J

# J = M/0.91

comprimento = float(input('Digite o comprimeto a ser convertido: '))

while True:# Para fazer o laço o parametro deve ser True, enquanto a condição for ele faz as converões.

    conversao = int(input('Digite 1 para converter em Metros ou 2 para converter em Jardas: '))

    if conversao == 1:
        metros = float(.91 * comprimento)
        print(f'Para {comprimento} Jardas Temos %.2f' %metros,'Metros.')
        break
    elif conversao == 2:
        jardas = float(comprimento/0.91)
        print(f'Para {comprimento} Metros Temos %.2f' %jardas, 'Jardas.')
        break

    print('Digite um valor valido!!!')
