"""
        Erros mais comuns em Python


Os erros mais comuns:

1 - SyntaxError - > Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem.

Exemplos SyntaxeError

a)
def funcao:
    print('Geek University')

b)
def = 1  (Uso de palavras reservadas a linguagem.)

c)
return


2 - NameError -> Ocorre quando uma variável ou função não foi definido.

Exemplos NameError

a)
print(Geek) (Tentando imprimir uma variável que não foi definida)

b)
geek()  (Tentando invocar uma função que não foi definida.)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a)
print(len(5)) Erro len() não faz a ação em um inteiro.

b)
print('Geek' + []) Erro ao tentar concatenar uma string a uma lista vazia ou inteiro.

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dados indexados
utilizando um ínidice inválida.

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
tupla = ('Geek')
print(tupla[0][10])


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) reebe um argumento com tupo correto
mas valor inapropriado.

Exemplos ValueError

a)
print(int('Geek')) Tentando converter uma string para inteiro.



6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.u

Exemplos de KeyError

a)
dic = {'python': 'university'} Tentando acessar o valor de uma chave que não existe.
print(dic['geek']

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função .

Exemplos de AttributeError

a)
tupla = (11, 22, 33, 55, 66) O erro ocorre pois o atributo sort() só é utilizado em listas e não tupla.
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

a)

def nova():
print('Geek') #IndentationError: expected an indented block

nova()

b)
for i in range(10):
i + 1  #IndentationError: expected an indented block

"""



