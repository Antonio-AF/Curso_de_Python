print("***Para sabermos quantas bolinhas de isopor cabem em um caixa de lados iguais, devemos calcular \n"
      "o volume da caixa e o volume das bolinha de isopor, posteriormente dividir o valor do volume da caixa pelo \n"
      "volume das bolinhas***")

# Solicita do usuário o raio da bolinha de ispor.
raioR = float(input("Digite o valor para o Raio das bolinhas em cm: "))
a = int(input('Digite a medida de um dos vertices da caixa: '))


# Função que calcula o volume da esfera.
def v_esfera(raioR):
    pi = 3.141592
    raioR = raioR ** 3
    return float(4 / 3 * pi * raioR)


print(f'O volume de cada bolinha é {v_esfera(raioR): .2f}cm³')


def v_cubo(a):
    return a**3


print(f'O volume da caixa é de {v_cubo(a)}cm³')


def quantidade_de_bolinhas(v_cubo, v_esfera):
    return v_cubo//v_esfera


print(f'A quantidade de bolinha na caixa é de {quantidade_de_bolinhas(v_cubo(a), v_esfera(raioR))} unidades')