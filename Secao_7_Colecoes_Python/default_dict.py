"""
Módulo Collections - Default Dict

# Recapitulando Dicionários.

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

Default Dict - > Ao criar um dicionário utilizando-o, nós informamos um valor default,
podemos utlizar um lambda para isso. Este valor será utilizado sempre que nçai houver um valor
definido. Caso tentarmos acessar uma chave que não existe, essa chave será criada e o valor
default será atribuído.

OBS: Lambdas são funções sem nomes, que podem ou não receber parâmetros de entrada e retorna valores.
"""

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)



dicionario['curso'] = 'Progração em Python: Essencial'

print(dicionario)

print(dicionario['curso'])
print(dicionario['outros']) # KeyError no diciobnário comum, mas aqui não retorna o erro.
print(dicionario)