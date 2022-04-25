"""
Conjuntos

- Conjuntos em qualquer linguagem de programação,
estamos fazendo referência á Teoria dos Conjuntos

- qui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática.

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos
se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionbarios) em Python:
    - Um dicionário em Chave/Valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS:. Ao criar um conjunto, caso seja adicionao um valor já existente, o mesmo será
# ingnorado sem gerar error e não fará parte do conjunto.

# Foma 2 - Mais comum

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# importante lembrar que, além de não termos valores duplicados, não temos ordem.


dados = '99', '2', '34', '23', '2', '34', '12', '1', '44', '5'

# Listas aceitam valores duplicados, então temos 10 elementos.
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos.
tuplas = tuple(dados)
print(f'Tupla: {tuplas} com {len(tuplas)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elemntos.
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valore duplicados, então temos 8 elementos.
conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets.

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um sets normalmente.

for valor in s:
    print(valor)

# Usos interessantes com sets.

# Imagine que fizemos um formulários de cadastro de visitantes em uma feira ou museu,
# e os visitantes informam manualmente as cidades de onde vieram.

# Nós adicionbamos cada cidade em uma lista Python , já que em uma lista
# podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba',
           'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unica temos.

# O que você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto.

s = {1, 2, 3}
print(s)
s.add(4)
s.add(4) # Duplicitade não gera error. Simplesmente é ignorado e não é adicionado.
s.add('4') # Se o elemento for uma String ele aceita.
s.add(2*(8-2)) # Aceita adicionar operações.

print(s)

# Remover elementos em um conjunto.

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # Não é indice informamos o valor a ser removido.

print(s)

# OBS:. Caso o valor não seja encontrado será gerado o erro Keyerror.
# Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)

# OBS:. Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)


s = {1, 2, 3}
print(s)

# podemos remover todos os itens de um conjunto.

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos.

# Imagine que temos dois conjuntos: Um contendo os estudantes do curso Python e um,
# contendo os estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjuntos com nomes deestudantes únicos.

# Forma 1 - Utilizando union (União)

#unicos1 = estudantes_python.union(estudantes_java)
# {'Gustavo', 'Fernando', 'Guilherme', 'Patricia', 'Pedro', 'julia', 'Ellen',
# 'Marcos', 'Julia', 'Ana'}

unicos1 = estudantes_java.union(estudantes_python)
#{'Pedro', 'Ellen', 'Ana', 'Gustavo', 'Guilherme', 'Marcos', 'julia',
# 'Julia', 'Patricia', 'Fernando'}

print(unicos1)

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java

print(unicos2)


# Gerar um conjunto de estudante que estão em ambos os cursos:

# Forma 1 - Utilizando o intersection.

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_java & estudantes_python
print(ambos2)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que não estão no outro curso.

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho.

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

