"""
    18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações
    matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o
    seu programa então pede dois valores numéricos e realiza a operação, mostrando
    o resultado e saindo.

"""

print('================================================')
print("/Please enter a number according to the menu!!!/")
print('================================================')

print("""
=================================================
        Essas são as Funções Disponiveis:
=================================================    
        (1) = Somar
        (2) = Subtrair
        (3) = Multiplicar
        (4) = Dividir
        
=================================================

    """)

op = int(input('Qual a função desejada? '))

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

if op == 1:
    soma = num1 + num2
    print(f'A soma dos numeros digitados é {soma}')
elif op == 2:
    sub = num2 - num1
    print(f'A diferença entre os numeros difitados é {sub}')
elif op == 3:
    mult = num1 * num2
    print(f'A multiplicação dos numero digitados é {mult}')
elif op == 4:
    div = num1/num2
    print(f'A divisaõ entre os numero digitados é {div}')
else:
    print('O numero digitado não corresponde a uma operação da Lista!!!')
