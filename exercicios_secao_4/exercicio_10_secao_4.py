# 10 - Leia uma velocidade em Km/h (quilômetro por hora) e apresente-a convertida em m/s.

#  M = K/3.6

velocidade = float(input('Digite a velocidade:'))

ms = float(velocidade/3.6)

print("A velocidade", velocidade, "km/h, em m/s é:", ms)
