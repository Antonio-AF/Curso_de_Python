
"""
    26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
    calcule o consumo e Km/l e escreva uma mensagem de acordo com a tabela abaixo:

       ##################################
       ##Consumo /  (Km/L)  /  Mensagem##
       ##################################
        menor que  8        Venda o carro!
        entre       8 e 14   Econômico!
        maior que    12      Super econômico!


"""

distancia = float(input('Digite a Distância percorrida em Km: '))
litro = float(input('Digite quantos litros foi consumido: '))

consumo = distancia/litro


def consumo_gasolina(consumo):
    if consumo < 8:
        print('Venda o Carro!!!')
    elif 8 <= consumo <= 14:
        print('Seu carro é Econômico')
    elif consumo > 12:
        print('Seu carro é Super Econômico!!!')
    else:
        print('Digite um valor valido')


consumo_gasolina(consumo)