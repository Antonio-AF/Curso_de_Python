""""
    22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
    As condições para aposentadoria são.

    * Ter pelo menos 65,
    * Ou ter trabalhado eplo menos 35 anos,
    * Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

"""

idade = int(input('Digite sua idade: '))
tempo_de_servico = int(input('Digite seu tempo de serviço: '))


def aposenta(idade, tempo_de_servico):
    if idade >= 65:
        print('Você pode se aposentar!!!')
    elif tempo_de_servico >= 35:
        print('Você pode se aposentar!!!')
    elif idade >= 60 and tempo_de_servico >= 25:
        print('Você pode se aposentar!!!')
    else:
        print('Você não tem idade nem tempo de tempo de trabalho para se aposentar!!!')


aposenta(idade, tempo_de_servico)

