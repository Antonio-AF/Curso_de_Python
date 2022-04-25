# 38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
# sabendo que ele recebeu um aumento de 25%.

salario = float(input('Digite o salário do Funcionário: '))

aumento = float(salario+((salario * 25)/100))

print('O salario com aumento é: ', aumento)
