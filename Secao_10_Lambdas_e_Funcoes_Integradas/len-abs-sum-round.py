"""
Len, Abs, Sum, Round.

# Len

len() -> Retorna o tamnho (ou seja, o número de itens) de um interável.

abs() -> Retorna o valor absoluto de um número interio ou real. De forma básica, seria o seu valor real sem o sinal.

sum() -> Recebe como parametro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor valor inicial.

OBS: O valor inicial default = 0

round() -> Retorna um número arrendodado para n digito de precisão após a casa decima, Se a precisão não for informada
retorna o inteiro mais próximo da entrada.

"""

# Só para revisar.

print(len('Geek University'))

print(len([1, 2, 3, 4, 5, 6, 8]))

print(len((1, 2, 5, 9, 6, 8, 4, 7)))

print(len({1, 2, 3, 6, 5, 4, 9, 8, 7}))

print(len({'a': 1, 'b': 2, 'c': 5, 'd': 8}))

print(len(range(0, 100)))

# por debaixo do spanos, quando utilizamos a função len() pm Python faz o seguinte:
# Dunter len, são funções especiais do Python
print('Geek University'.__len__())

print('####################################################\n\n')

# Exemplo Abs

print(abs(-5))
print(abs(5))
print(abs(-895))

print('####################################################\n\n')

# Exemplos Sum

print(sum([1, 2, 3, 4, 5, 6]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.899]))

print(sum((1, 2, 3, 6, 6, 5, 5, 5, 5,)))

print(sum({1, 2, 3, 5, 75, 9, 4563, 55622}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 75, 'f': 9, 'g': 4563, 'h': 55622}.values()))

print('####################################################\n\n')

# Exemplo Round

print(round((3.145 + 5.899)))

print(round(0,1574))

print(round(0.999999))

print(round(1.2121212121, 2))

print(round(1.219999, 2))