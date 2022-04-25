# 24 e 25 Leia um valor de área em metros quadrdos m² e apresente-o convertido em acres, e vice-versa.

# A = M * 0.000247
# M = A * 4048.58

area = float(input('Digite a area a ser convertida: '))

while True:

    opcao = int(input('Digite 1 para converter em Acres, Digite 2 para conerter para Metros Quadrados: '))

    if opcao == 1:

        metrosqu = float(area * 4048.58)
        print(f'A area {area} Acres convertida para m² %.3f é:' %metrosqu)
        break
    elif opcao == 2:

        acres = float(area * 0.000247)
        print(f'A area {area} m² convertida para Acre %.3f é:' %acres)
        break

    print('Digite uma opção valida')
