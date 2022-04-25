# 11 - Leia uma velocidade em m/s(metros por segundos) e apresente-a convertida em km/h.

# Km/h = 1.61 * Metros/s.

velocidade = float(input("Digite a velocidade:"))

kmporhora = 1.61 * velocidade

print("A velocidade", velocidade, "M/s é", kmporhora,'Km/h')
