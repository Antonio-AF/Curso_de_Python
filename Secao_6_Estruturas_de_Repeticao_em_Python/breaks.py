"""
Saindo de lopps com o  break

Funciona da mesma forma que nas limguagens C o Java.

Utilizamos o break para sair de lopps de manieira projetada.

"""

# Exemplo 1

for numero in range(1, 100):
    if numero == 66 + 1:
        break
    else:
        print(numero)
print('Sai do loop')


# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
