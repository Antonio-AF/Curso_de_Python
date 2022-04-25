"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como o def ou qualquer outra em Python.o

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma greal de utilização é:

raise TipoDoErro('Menssagem de erro')


Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Antonio', 'Azul')


# Exemplo refatorado.


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise TypeError(f'A cor precisa ser uma dentre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Antonio', 'azul')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise TypeError(f'A cor precisa ser uma dentre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

    
colore('Antonio', 'azul')