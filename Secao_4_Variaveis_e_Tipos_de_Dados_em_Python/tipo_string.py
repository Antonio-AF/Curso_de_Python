"""
Tipo String.

Já vimos que em Python um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'Nome', '222', 'a', 'True', '12.3'
- Sempre que estiver entre aspas duplas -> "nome", "222", "a", "True", "12.3"
- Sempre que estiver entre aspas simples triplas -> '''nome''', '''1222''', '''s''', '''True''', '''12.58'''
- Sempre que estiver entre aspas duplas triplas -> Da mesma forma porem utilizando as

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Ginas's Bar"
print(nome)
print(type(nome))

nome = '"Angelina Jolie"'
print(nome)
print(type(nome))

nome = 'Geek university'
print(nome.upper()) # .upper trasnforma para maiuscula todas as letras

nome = 'Geek University'
print(nome.lower()) # .lower trsforma para minuscula todas as letras

nome = 'Geek University'
print(nome.split()) # .split trsforma em lista e separa cada palavra por virgula.

# Projeto numeros primos

num = '187'
print(num[0])

soma = int(num[0]) + int(num[1]) + int(num[2])

print(soma)
"""
# Slice de String

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
""""""
nome = 'Geek University'
print(nome[0])

print(nome[::-1]) # Invertendo a String.

