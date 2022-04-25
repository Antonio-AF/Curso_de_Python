'''
    13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
    A primeira e segunda nota têm peso 1 e a terceira nota tem peso 2. Ao final,
    mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
    A nota para aprovação de ser igual ou mair que 60 pontos.
'''

nota1 = float(input('Digite a Nota da Prova 1: '))
nota2 = float(input('digite a nota da Prova 2: '))
nota3 = float(input('Digite a Nota da Prova 3: '))

# Pesos das notas
p1 = 1
p2 = 1
p3 = 2

mediap = (p1 * nota1)+(p2 * nota2)+(p3 * nota3)/ (p1 + p2 + p3)

if mediap >= 60:
    print(f'Você foi aprovado com média {mediap}, parabens!!!')
else:
    print(f'/n Você obteve uma médoa de {mediap} e foi reprovado.')


