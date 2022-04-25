"""
    Pacotes

Módulo -> É apenas um aquivos Python que pode ser diversas funções para utilizarmos:

Pacote - > É um diretório contendo uma coleção de módulos;


OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo
chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo, mas
normalmente ainda é utilizado para manter compatibilidade.

"""

from geek.geek1 import funcao1
from geek.university import geek3, geek4

#print(geek1.pi)

funcaoB = funcao1(45, 45)
print(funcaoB)

#print(geek1.funcao1(5, 5))

#print(geek2.curso)
#print(geek2.funcao2())

print(geek3.funcao3(), geek4.funcao4())
