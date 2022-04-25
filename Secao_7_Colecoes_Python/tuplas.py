"""

Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básica:

1 - As tuplas são representadas por parênteses ().

1 - As tuplas são imutaveis: Isso sifnifica que as se criar uma tupla ela nçao muda. Toda operação
em uma tupla gera uma nova tupla.

# CUIDADO 1 : As tuplas são representadas por (), mas veja.

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print((tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)
print(tupla3)

print(type(tupla3))


tupla5 = 4,
print(tupla5)

print(type(tupla5))

# CONCLUSÂO: Podemos concluir que tuplas são definidas pela vírgula e não pelos parêmteses.

(4) --> Não é Tupla.
(4,) --> É Tupla.
4, --> É Tupla.


# Podemos gerar uma tupla dinamicamente com o range(inicio, fim, passo).

tupla = tuple(range(11))
print(tupla)

print(type(tupla))


# Desempacotamento de Tuplas.

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Obs: Gera erro (ValueError) se colocarmos um número diferente de ementos para desacomplamento.


# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das Tuplas serem imutaveis.

# Soma*, Valor Máximo, Valor Mínimo* e Tamanho.

# * Se os valore forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 'b')

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de Tuplas.

tupla1 = (1, 2, 3)

print(tupla1)

tupla2 = (4, 5, 6)

print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis.

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2

print(tupla1) # Tuplas são imutáveis, mas podemos sobreescrever seus valores.

# Verificando se determinado elemento está contido na tupla.


tupla = (1, 2, 3)
print(3 in tupla)


# Iterando sobre uma tupla.

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contando elementos dentro de uma tupla.

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas.

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados em uma coleção.

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

# O acesso a elementos de uma tupla também pe semlhante a de uma lista.

print(meses[5])

# Iterando com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificando em qual indice um elemento na tupla.

print(meses.index('Julho'))

# Obs: Caso o elemento não exista, será gerado ValueError.


# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

"""

# Por que utilizar Tuplas?

#  - Tuplas são mais rápidas do que listas.
#  - Tuplas deixam seu codigo mais seguro*.

# Isso porque trabalhar com elementos imutáveis traz segurança para o código.


# Copiando uma tupla para outra.

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy.

print(nova)
print(tupla)

outra  = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
