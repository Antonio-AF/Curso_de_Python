#  15 - Leia um ângulo em radianos e apresente-o convertido em graus.

# G = R * 180/Pi.

angulo = float(input("Digite o ângulo a ser convertido:"))

pi = 3.141592
graus = float(angulo*(180/pi))

print("O ângulo digitado em radianos é %.2f" %graus, '°')

