# 45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
# ASCII para reslver o problema.

def paraMinuscula(c):

    if c >= 'A' and c <= 'Z':

        return chr(ord('a') + ord(c) - ord('A'))
    else:
        return c

texto = input('Digite um texto: ')

textoMinusculo = ''

for l in texto:

    textoMinusculo += paraMinuscula(l)


print('Em Minúsculo: ')
print(textoMinusculo)
