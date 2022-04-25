# 40 - Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o número de dias trabalhados
# pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

dias = int(input('Digite os dias Trabalhados: '))

valor_dia = 30

salario = float(dias * valor_dia)

imposto = float((salario * 8)/100)

liquido = salario - imposto

print('O Salário líquido a receber com desconto do IR é de R$', liquido)
