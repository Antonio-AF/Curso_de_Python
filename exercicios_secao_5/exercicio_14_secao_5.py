'''

    14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
    de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
    final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2;
    Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno foi reprovado
    (média entre 0 e 2,9), de recuperação (entre 3 e 4,9)ou se foi aprovado. Faça todas as verificações
    necessárias.

'''

lab = float(input('Digite a sua note do Trabalho de Laboratório: '))
ava_sem = float(input('Digite sua nota da Avaliação Semestral: '))
exame_final = float(input('Digite sua nota do Exame Final: '))

p1 = 2
p2 = 3
p3 = 5

mediap = (p1 * lab) + (p2 * ava_sem) + (p3 * exame_final) / (p1 + p2 + p3)

if lab and ava_sem and exame_final <= 10:

    if mediap > 5:
        print(f'Sua média foi de {mediap} e você foi aprovado!!!')

    elif 3 >= mediap <= 4.9:
        print(f'Sua média foi {mediap} e você está de Recuperação!!!')

    else:
        print('Você foi reprovado.')

else:
    print('Digite uma nota valida!!!')

