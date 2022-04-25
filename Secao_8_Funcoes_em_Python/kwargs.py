"""
            ::: **KWARGS:::

Poderiamos chamar o parâmetro de **xix, mas por convenção chamamos de **kwargs.

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwrags exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
      print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certexa quem é você . . . '

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


# Nas nossas funções, podemos ter: (NESTA ORDEM):

# - Parâmetros obrigatórios:
# - *args;
# - Parâmetros default (não obrigatórios);
# - **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é iportante manter a ordem dos parâmentros na declaração

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com o **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

"""


def soma_multiplus_numeros(a, b, c, *args):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplus_numeros(*lista)
soma_multiplus_numeros(*tupla)
soma_multiplus_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplus_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário deven ser os mesmos dos parametros da função.

#dicionario = dict(d=1, e=2, f=3) # TypeError
# soma_multiplos_numeros(**dicionario)




