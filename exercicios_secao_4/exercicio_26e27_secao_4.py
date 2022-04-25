# 26 e 27 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares, e vice-verssa

# H = M * 0.0001 Converte para hectar.
# M = H * 10000 converte para Metros Quadrados.

area = float(input('Digite a área a ser convertida: '))

while True:

    opcao = int(input('Digite 1 para converter para Hectar,'
                      'Digite 2 para converter para Metros Quadrados.'))
    if opcao == 1:

        h = float(area * 0.0001)
        print(f" A area {area}m² convertida para Hectares é de %.3f:" %h)
        break

    elif opcao == 2:

        m = float(area * 10000)
        print(f"A area {area}Hectares convertida para Metros Quadrados é de %.3f: " %m)
        break

    print('Digite uma opção valida!!!')
