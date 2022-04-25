# 14 - Leia o ângulo em graus e apresente-o convertido em radianos.

# R = G* PI/180

angulo = float(input('Digite o Ângulo a ser convertido para Radianos:'))

pi = 3.141592
radianos = float(angulo*(pi/180))


print("O ângulo digitado em radianos é %.2f:" %radianos)

