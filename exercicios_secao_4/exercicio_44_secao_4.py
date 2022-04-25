# 44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
# Calcule e mostre quantos degraus o usuário deverá subvir para atingir o seu objetivo.


altura_degrau = float(input('Digite a altura de cada de grau em cm: '))

altura_alcancar = int(input('Digite a altura que deseja alcançar em cm: '))

quantidade = float(altura_alcancar / altura_degrau)

print(f'Você terá que subir {quantidade} para atingir seu objetivo.')

