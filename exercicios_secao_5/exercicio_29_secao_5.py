"""
    29 - Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros
    menores do que 100. Escolha números aleátorios entre 1  e 100, e mostre na tela a pergunta: qual
    é a soma de a + b, onde a e b são os números aleátorios. Peça a resposta. Faça cinco perguntas ao
    aluno, e mostre para ele as perguntas e as respostas corretas, além de quatas vezes o aluno
    acertou.

"""
from random import randint

print('Responda as questões ')


def questao_1():
    a = randint(1, 100 + 1)
    b = randint(1, 100 + 1)

    global questao1
    questao1 = str(f'1) Qual é a soma de {a} + {b}? ')
    print(questao1)

    global soma_R1
    soma_R1 = int(a + b)

    global R1
    R1 = int(input('R = '))


questao_1()


def questao_2():
    a = randint(1, 100 + 1)
    b = randint(1, 100 + 1)

    global questao2
    questao2 = str(f'2) Qual é a soma de {a} + {b}? ')
    print(questao2)

    global soma_R2
    soma_R2 = int(a + b)

    global R2
    R2 = int(input('R = '))


questao_2()


def questao_3():
    a = randint(1, 100 + 1)
    b = randint(1, 100 + 1)

    global questao3
    questao3 = str(f'3) Qual é a soma de {a} + {b}? ')
    print(questao3)

    global soma_R3
    soma_R3 = int(a + b)

    global R3
    R3 = int(input('R = '))


questao_3()


def questao_4():
    a = randint(1, 100 + 1)
    b = randint(1, 100 + 1)

    global questao4
    questao4 = str(f'4) Qual é a soma de {a} + {b}? ')
    print(questao4)

    global soma_R4
    soma_R4 = int(a + b)

    global R4
    R4 = int(input('R = '))


questao_4()


def questao_5():
    a = randint(1, 100 + 1)
    b = randint(1, 100 + 1)

    global questao5
    questao5 = str(f'5) Qual é a soma de {a} + {b}? ')
    print(questao5)

    global soma_R5
    soma_R5 = int(a + b)

    global R5
    R5 = int(input('R = '))


questao_5()


print('Gabarito das Questões!!!\n')

v = 0
f = 0

if R1 == soma_R1:
    print('Você acertou')
    print(questao1)
    print(f'A resposta dada foi {R1}.')
    print(f'Gabarito da questão é {soma_R1}.\n')
    v += 1

else:
    f += 1

if R2 == soma_R2:
    print('Você acertou')
    print(questao2)
    print(f'A resposta dada foi {R2}.')
    print(f'Gabarito da questão é {soma_R2}.\n')
    v += 1
else:
    f += 1

if R3 == soma_R1:
    print('Você acertou')
    print(questao3)
    print(f'A resposta dada foi {R3}.')
    print(f'Gabarito da questão é {soma_R3}.\n')


else:
    f += 1

if R4 == soma_R4:
    print('Você acertou')
    print(questao4)
    print(f'A resposta dada foi {R4}.')
    print(f'Gabarito da questão é {soma_R4}.\n')
    v += 1
else:
    f += 1

if R5 == soma_R5:
    print('Você acertou')
    print(questao5)
    print(f'A resposta dada foi {R5}.')
    print(f'Gabarito da questão é {soma_R5}.\n')
    v += 1
else:
    f += 1


print(f'Você teve {v} acertos e {f} erros.')
