"""
    27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias.txt

    Infantil A  5 a 7
    Infantil B  8 a 10
    Juvenil  A  11 a 13
    Juvenil  B  14 a 17
    Sênior      Maiores de  18 anos.
"""

print('Para saber sua Classificação informe sua idade abaixo!!!')

idade = int(input('Digite sua Idade: '))

if 5 <= idade <= 7:
    print(f'Você tem {idade} anos e pertence a Classe Infantil A')
elif 8 <= idade <= 10:
    print(f'Você tem {idade} anos e pertence a Classe Infantil B')
elif 11 <= idade <= 13:
    print(f'Você tem {idade} anos e pertence a Classe Juvenil A')
elif 14 <= idade <= 17:
    print(f'Você tem {idade} anos e pertence a Classe Juvenil B')
elif idade >= 18:
    print(f'Você tem {idade} anos e pertence a Classe Sênior')
else:
    print('Digite uma Idade Valida')

