# 41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
# trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

valor_hora = float(input("Digite o valor da Hora: R$"))
horas_trabalhadas = float(input("Digite as Horas Trabalhadas: "))

salario = (valor_hora * horas_trabalhadas)

salario = float(salario+((salario * 10)/100))

print("Você receberá de Salário R$", salario)
