# 8 - Faça um programa que leia2 notas de um aluno, verifique se as notas são
# válidas e exiba na tela a média destas notas. Uma nota válida deve ser,
# obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um
# valor válido, este fato de se infomado ao usuário e o programa termina.

nota1 = float(input('Digite sua Nota A1: '))
nota2 = float(input('Digite sua Nota A2: '))

if (nota1 >= 0.0) and (nota1 <= 10.0):

    if (nota2 >= 0.0) and (nota2 <= 10.0):

        media = (nota1 + nota2)/2
        print('A média das Notas Digitadas é: ', media)

    else:
        print('As notas digitadas não são validas!!!')

