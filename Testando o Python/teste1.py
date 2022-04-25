#num = input('Digite uma sequencia crescente:')

#print(num[0:5], num[5:11])

"""
def paraMaiuscula(c):
    if c >= 'a' and c <= 'z':
        return chr(ord('A') + ord(c) - ord('a'))
    else:
        return c


def paraMinuscula(c):
    if c >= 'A' and c <= 'Z':
        return chr(ord('a') + ord(c) - ord('A'))
    else:
        return c


# PROGRAMA PRINCIPAL
texto = input("digite um texto: ")  # Suponha que o usuário digitou "PeQuEno TesTE"

textoMaiusculo = ''
textoMinusculo = ''
for l in texto:
    textoMaiusculo += paraMaiuscula(l)
    textoMinusculo += paraMinuscula(l)

print("Em maiúsculas: ")
print(textoMaiusculo)

print("Em minúsculas: ")
print(textoMinusculo)

"""

num = int(input('Digite o número que deseja converter em Binário: '))

i = 1


while i >= 1:


    i = int(num / 2)

    print(i)

    resto = int(num % 2)
    print(resto)

