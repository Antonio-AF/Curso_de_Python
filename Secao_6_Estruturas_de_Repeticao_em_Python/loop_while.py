"""
Loop while


Forma geral

while expressão_booleana:
    //execção do loop


O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana e toda expressão onde o resultado é verdadeiro ou falso:

Exemplo:

num = 5

num < 5

# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Obs: Em um loop while, é importante que cuidemos do critério de parada, para não causar um loop infinito.


"""
# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Ja acabou Jéssica?')

