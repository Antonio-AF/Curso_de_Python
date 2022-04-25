"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
DINÂMICO e tambem de podermos coloar QUALQUER tipo de dado.

Linguagens C/JAVA : Arrays

    -Possuem tamanho e tipo de dado fixo.
    Ou seja, nestas linguagens se você criar um arrau do tipo int e com tamanho 5, este array será
    SEMPRE do tipo inteiro e poderá ter SEMPRE no máxiomo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas po colchetes: []

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado calor está contido na lista.
num = 9


if num in  lista4:
        print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista.
lista1.sort()
print(lista1)


# Podemos facilmente contar o número de ocorrências de um valor em um lista.

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas.

Para adicionar elementos ou valores em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# Obs: Com o append, nós só conseguimos adicionar 1 elemento por vez.
# lista1.append(12, 13, 45) Erro

lista1.append([8, 3, 1]) # Coloca a lista como elementos único (sub-lista).
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a Lista')
else:
    print('Não encontrei a Lista')


lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional a lista.
print(lista1)


num = list(input('Digite uma valor:'))

print(num) # Os valores digitados são convertidos para String dentro da lista.

if num[2] == '7': # Aqui verificamos se o numero na posição determinada é igual a 7.
    posicao2 = int(num[2]) # Transforma a String em um Inteiro.
    print('O número na posição 2 é igual a', posicao2)
else:
    print('Está Errado.')

num = int(input('Digite um numero maior quê 10: '))


if num > 10 and num < 100:

    num1 = int(num/10)
    num2 = int(num/10)
    if num1 == num2:
        print(num1 + num2)


# Podemos inserir um novo elemento na lista informando a posição do índice

# Obs: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.

lista1.insert(2, 'Novo Valor')
print(lista1)


# Podemos facilmente juntar duas listas.

lista1 = lista1 + lista2
#lista1.extend(lista2)
print(lista1)

#  Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2

print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista.
print(len(lista5))


# Podemos remover facilmente o último elemento de uma lista
# Obs: o pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# Obs: Os elementos á direita deste índice serão deslocados para a esquerda.
# Obs: Se não houver elementos no índice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)



# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista.

nova = [1, 2, 3, 4]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: Por padrão , o split separa os elementos da lista pelo esoaço entre elas.

# Exemplo 2

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split(',')
print(curso)


# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elçemento e trnsforma em uma string.
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca $ entre cada elçemento e trnsforma em uma string.
curso = '$'.join(lista6)
print(curso)


# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados.

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 41454654]
print(lista6)
print(type(lista6))

# Iterando sobre lista

# exemplo 1 Utilizando o for

for elemento in lista1:
    print(lista1)

# Exemplo 2 - Utilizando o while

carrinho = []
produto = ''

while produto != 'sair':

    print("Adicione um produto na lista ou digite 'sair para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variáveis em lista

numeros = [1, 2, 3, 4, 5]

print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada.

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # Verde
print(cores[1]) # Amarelo
print(cores[2]) # Azul
print(cores[3]) # Branco

# Fazermos acesso aos elementos de forma indexada inversa

print(cores[-1]) # Branco
print(cores[-2]) # Azul
print(cores[-3]) # Amarelo
print(cores[-4]) # Verde
#print(cores[-5]) # Error, pois não existe o índice -5


cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas também úteis.

# Encontrar o índice de um elemento na lista.

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?

print(numeros.index(6))

# Em qual índice da lista está o valor 9?

print(numeros.index(9))

#print(numeros.index(19)) # Gera ValueError

# Obs: Caso não tenha este elemento na lista, será apresentado erro ValueError.

# Obs: Retorna o índice do primeiro elemento encontrado.
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indie começar a busca.

print(numeros.index(5, 1)) # buscando a partir do índice 1
print(numeros.index(5, 2)) # buscando a partir do índice 2
print(numeros.index(5, 3)) # buscando a partir do índice 3

# Obs: Caso não tenha este elemento na lista, será apresentado erro ValueError.
#print(numeros.index(5, 4)) # buscando a partir do índice 4

# Podemos fazer buscas dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))


# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice  1 e pegando todos os relementos restantes.

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # Começa em 0, pega até o índice 2 - 1.

print(lista[:4]) # Começa em 0, pega até o índice 4 - 1.

print(lista[1:3]) # Começa em 1, pega até o índie 3 - 1.

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2.

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2.

# Invertendo valore em uma lista.

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)


# Soma, Valor Máximno*, Valor Mínimo*, Tamnho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # Soma.
print(max(lista)) # Máximno valor.
print(min(lista)) # Mínimo valor.
print(len(lista)) # Tamanho da lista.


# Podemos transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Podemos fazer o desempacotamento de listas.

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Obs: Se tivermos um número difernete de elementos na lista ou variáveis para receber os dados, teremos ValueError.


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas eles
# ficaram totalmente independente, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (copia profunda)
"""



# Forma 2 - Shalloe Copy

lista = [1, 2, 3]
print(lista)

nova = lista # Copia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar a modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # Soma.
print(max(lista)) # Máximno valor.
print(min(lista)) # Mínimo valor.
print(len(lista)) # Tamanho da lista.