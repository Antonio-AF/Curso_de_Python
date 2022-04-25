# 21 - Leia um valor de massa em libras e apresente-o convertido em quilograma.

#  K = L * 0.45

massa = float(input('Digite a massa a ser convertida: '))

conversao = int(input('Digite 1 para Converter em Libras ou 2 para converter em Quilograma: '))

libras = 1
quilogramas = 2

if conversao == 1:
    l = float(massa/0.45)
    print(f'Para {massa} kg temos', l,'libras')
elif conversao == 2:
    k = float(massa * 0.45)
    print(f'Para {massa} libras temos', k, 'kg')
