""""
            ::: ENTENDENDO O *ARGS:::

- O *args é um parâmetro, como outro qualquer. Isso siginifica que você poderá
chamar de qualquer coisa, desde que começe com asterisco

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utiliza em uma função, coloca os valores extras informados como entrada
em uma tupla. Então desde já lembre-se que tuplas são imutáveis.


# Exemplos

def soma_todos_numeros(num1, num2=4, num3=6, num4=10):
    return num1 + num2 + num3 + num4


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(9, 77, 45, 69))

# Entenendo o *args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 6))
print(soma_todos_numeros(7, 8, 9))
print(soma_todos_numeros(58, 63, 458, 963))


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek!!!'
    return 'Eu não tenho certeza quem é você ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""


def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 1205]

# Utilizamos o desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma. ele saberá
# que precisará antes desempacotar estes dados.

