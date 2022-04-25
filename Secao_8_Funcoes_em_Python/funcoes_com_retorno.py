"""
            :::Funções com Retorno:::



numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop:{ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')


OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None.

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra resernvada 'return'

OBS: Não precisamos necessáriamente criar uma variável para receber o retorno de
uma função. Podemos passar a execução da função para outras funções.


# Exemplo função => Vamos refatorar esta função para que ela retorne o valor.

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno:{quadrado_de_7()}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi'


alguem = 'Pedro!!!'


print(diz_oi())
print(alguem)


OBS: Sobre a palavra reservada return:

1 - Ela finaliza a função, ou seja, ela sai daexecução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tio de dado e até mesmo múltiplos valores;


# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes do retorno...') #Tudo que for antes do return será mostrado.
    return 'Oi!'
    print('Estou sendo executado após o retorno...') #Nada após o retorno é mostrado.


print(diz_oi())


# Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3

def outr_funcao():
    return  2, 3, 4 , 5


#num1, num2, num3, num4 = outr_funcao()
#print(num1, num2, num3, num4)

print(outr_funcao())
print(type(outr_funcao()))


# Vamos criar uma função para jogar uma moeda.

from random import  random

def joga_moeda():
    # Gera um número pseudo-randomico entre 0 e 1
    #valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'
print(joga_moeda())
"""

# Erros comuns na utilizaçao do retorno, que na verdade nem é erro, mas sim codificação descessária.

def eh_impar():
    numero = 3
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())