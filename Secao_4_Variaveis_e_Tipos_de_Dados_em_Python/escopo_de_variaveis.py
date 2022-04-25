"""
Escopo de Variaveis.

Dois casos de escopo:

1 - Variáveis  Globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.


2- Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado so bloco onde foi declarada.

Para declarar uma variável em Python faemos:

nom_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que aodeclarrmos uma vaiavel, nós não colocamos
o tipo de dado dela.

Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java;
int numero = 42;

"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))


