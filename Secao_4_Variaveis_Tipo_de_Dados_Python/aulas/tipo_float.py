
# Errado do poto de vista do Float
valor = 1, 44

print(valor)

# Certo do ponto de vista Float

valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição

valor1, valor2 = 1.44, 0
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int

"""
Obs: Ao converter valores float para inteiro, nós perdemos precisão.
"""

res = int(valor)
print(res)
print(type(res))

#  Podemos trabalhar com números complexos
variavel = 5j
