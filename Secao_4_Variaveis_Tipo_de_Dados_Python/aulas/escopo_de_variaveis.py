print("VARIÁVEIS DE ESCOPO GLOBAL!")

x = 10
y = 29


def soma(x, y):
    return x + y


def soma2():
   return print(f'A soma de {x} + {y} =', x + y)



def mult(x, y):
    return x * y


print(soma(x, y))
print(mult(x, y))
print(soma(345, 123))
soma2()

print("VARIÁVEIS DE ESCOPO LOCAL!")


def somaLocal():
    x = 17
    y = 34
    return x + y


def multLocal():
    x = 17
    y = 34
    return x * y


print(somaLocal())
print(multLocal())

