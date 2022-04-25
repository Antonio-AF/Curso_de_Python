
# Pegando duas entradas de cada vez
x, y = [int(x) for x in input("Entre com dois valores: ").split()]
print("Um número para X: ", x)
print("Um número pra Y: ", y)
print()


def soma(x, y):
    somar = x + y
    return somar


def sub():
    subtrair = x - y
    return subtrair


def mult(x, y):
    mults = x * y
    return mults


print(soma(x, y))
print(sub())
print(mult(x, y))


def factor(n):
    if n == 1:
        return 1
    return n * factor(n-1)


print(f'O Fatorial de 5 é {factor(5)}')
print(f'O Fatorial de 6 é {factor(6)}')
print(f'O Fatorial de 7 é {factor(7)}')
print(f'O Fatorial de 8 é {factor(8)}')
print(f'O Fatorial de 10 é {factor(10)}')