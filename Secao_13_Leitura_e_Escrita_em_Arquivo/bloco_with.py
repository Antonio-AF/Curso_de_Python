"""
O Bloco With


Passo para se trabalhar com arquivos.

# 1 - Abrirmos o arquivo;

# 2 - Manipulamos o arquivo;

# 3 - Fechamos o arquivo;

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados
após o bloco with.

"""

import json

name = input("Digite seu nome: ")
first_name = input("Digite seu Sobrenome: ")

x = {
    "nome": name,
    "Sobrenome": first_name,
    "idade": 36,
    "Cidade": "Florianopolis"
    }

y = json.dumps(x)
z = json.loads(y)


print(y)
print(z["nome"])
print(z["Sobrenome"])
print(z["idade"])

# O Bloco with - Forma Pythônica de manipular arquivo

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


