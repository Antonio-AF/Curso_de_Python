"""
            ### Set Comprehension ###

Lista = [1, 2, 3, 4, 5]

set = {1, 2, 3, 4, 5}


"""

# Eemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outros exemplo

numeros = {x ** 2for x in range(10)}
print(numeros)

# Para colocarmos o resultados dentro de um dicionário colocamos X: antes do valor x **2

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para finalizar

letras = {letra for letra in 'Geek University'}

print(letras)