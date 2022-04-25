# 51 - Escreva um programa que leia as coordenadas x e y de pontos no R²e calcule sua distância da Origem.

x = int(input('Digite o valor da coordenda X: '))
y = int(input('Digite o valor da coordenada Y: '))

distancia = float((x**2 + y**2)**0.5)

print('A distancia da Origem é: ', distancia)
