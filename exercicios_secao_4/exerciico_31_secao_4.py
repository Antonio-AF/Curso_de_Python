# 31 - Leia um número interio e imprima o seu antecessor e sucessor.

num = int(input("Digite um numero:"))

sucessor = num + 1
antecessor = num - 1

print(f'O sucessor de {num} é {sucessor}, e o antecessor de {num} é', antecessor)
