# 9 - Leia o salário de um trabalhador e o valor da prestação de uma empréstimo.
# e a prestação for maior que 20% do salário imprima:
# Empréstimo não concedido, caso contrário imprima:
# Empréstimo concedido.

salario = float(input('Informe o salário: '))

prestacao = float(input('Informe o valor da Prestação: '))

controle = float((salario * 20)/ 100)


if prestacao < controle:
    print('Empréstimo concedido!!!')

else:
    print('Empréstimo não concedido!!!')

