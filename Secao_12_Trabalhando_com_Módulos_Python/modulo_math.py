import math
"""
#x = int(input('Digite um numero Inteiro maior que 0 : '))

print('Equação Quadratica ou  Baskara')

a = int(input('Digite um Valore para a: '))
if a == 0:
    a = int(input('Digite um numero Diferente de Zero: '))

b = int(input('Digite um Valore para b: '))

c = int(input('Digite um valor para c: '))


def equacao_quadratica():
    delta = (b ** 2 - 4 * a * c)
    raiz = math.sqrt(delta)
    return raiz

delta = equacao_quadratica()

print(delta)

x1 = (-b + delta) / 2*a

x2 = (-b - delta) / 2*a

print(f'A primeira Raiz da equação é {x1} ')
print(f'A segunda Raiz da equação é {x2} ')"""


s = float(input('Digite um expoente valido: '))
n = int(input('Digite um numero inteiro: '))

n_interaction = n
z_list = []
i = 0
z = 0

while i <= n_interaction:
    if n > 0:
        z = 1/n**s
        n = n - 1
        i = i + 1
        z_list.append(z)
    else:
        print('Divisão por zero')
        break

print(z)
print(z_list)

soma_z = 0
for z in z_list:
    soma_z += z

print(f' A soma de todos os Z é {soma_z}')
