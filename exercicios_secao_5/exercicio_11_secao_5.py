# 11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela a
# soma de todos os seu algarismos. Por exemplo, ao número 251 correspoderá o valor 8(2+5+1).
# Se o número lido for maior do que zero, o programa terminará com a mensagem "Número Inválido".

num = int(input('Digite um Número Maior que Zero: '))

if num > 0:
    num2 = str(num)
    num3 = list(num2)
    somar = int(num3[0]) + int(num3[1]) + int(num3[2])
    print('A soma dos algarismos do numero digitado é:', somar)

else:
    print('Número inválido')

