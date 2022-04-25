# 42 - Receba o salário-base de um funcionário. Calcule e impria o salário a receber, sabendo-se que esse funcionário
# tem uma gratificação de 5% sobre o salário-base.
# Além disso, ele paga 7% de imposto sobre o salário-base.

salario_base = float(input('Digite o Salário-Base do Funcionário: '))


bonus = float(salario_base + ((salario_base * 5)/100))

imposto = float((bonus * 7 )/100)

salario_receber = bonus - imposto

print("O salário a receber é de R$", salario_receber)
