# 36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
# O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = Pi * raio² * altura.

# Pi = 3.141592

raio = int(input('Digite o Raio do Cilindro: '))
altura = int(input("Digite a Altura do Cilindro: "))

pi = 3.141592

volume = float(pi*(raio**2 * altura))

print('O volume do cilindro é: ', volume)
