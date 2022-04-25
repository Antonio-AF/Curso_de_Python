"""
Tipo Booleano.

Algebra booleana, criada por George Boole

2 constante, Vertadeiro ou Falso.

True -> Verdadeiro
False -> Falso

Obs: Sempre com a primeira letra maiuscula.

Errado:

true, false

Certo:

True, False.
"""
ativo = False
logado = False

print(ativo)

# Operações básicas:

# Negação (not):

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.

"""
print(not ativo)

# Ou (or):

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro de ser verdadeiro.

True or True -> True.
True or False -> True.
False or True -> True.
False or False -> False.

"""
print(ativo or logado)

# E (end)

"""
Também é uma operação binária, ou seja, depende de dois valores. 
Ambos os valores devem ser verdadeiro.

True and True -> True.
True and False -> False.
False and True -> False.
False and False -> False.

"""