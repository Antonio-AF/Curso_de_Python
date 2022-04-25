# 10 - Faça um progrma que receba a altura e o sexo de uma pessoa e calcule e mostre seu
# peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):

# * Homens: (72,7 * h) - 58
# * Mulheres: (62,10 * h ) - 44,70

sexo = input("Digite M para Masculino e F para Feminino: ")
altura = float(input("Digite sua Altura: "))

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Com base na sua Altura de {altura} seu peso Ideal é {peso_ideal}Kg.")

elif sexo == 'F':
    peso_ideal = (62.10 * altura) - 44.70
    print(f'Com base na sua Altura de {altura} seu peso Ideal é {peso_ideal}Kg.')

else:
    print("As informações digitadas não são validas!!!")

