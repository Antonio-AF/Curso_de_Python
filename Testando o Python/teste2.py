valor = float(input('Insira o Valor do Produto.'))
est = int(input(f'Digite as iniciais correspondente ao seu Estado:'
                '\n (1) Minas Gerais\n (2) São Paulo \n (3) Riuo de Janeiro \n (4)Mato Grosso do Sul \n'))

MG = 7
SP = 12
RJ = 15
MS = 8

final1 = valor * MG / 100 + valor
final2 = valor * SP / 100 + valor
final3 = valor * RJ / 100 + valor
final4 = valor * MS / 100 + valor



if  est == 1:
    print(f'O valor do produto com o frete será R${final1}')


elif est == 2:
    print(f'O valor do produto com o frete será R${final2}')

elif est == 3:
    print(f'O valor do produto com o frete será R${final3}')

elif est == 4:
    print(f'O valor do produto com o frete será R${final4}')


else:
    print(f'Infelizmente nossa Empresa não faz Entregas no Seu Estado.')
