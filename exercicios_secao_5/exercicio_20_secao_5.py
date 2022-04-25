"""
    20 - Dados três valores, A, B, C verificar se eles podem ser valores dos lados de um triângulo
    e, se forem, se é um triângulo escaleno, equilátero ou isósceles.

"""
print("Digite os valore para os lados aseguir!")

ladoA = int(input("Lado A: "))
ladoB = int(input("Lado B: "))
ladoC =  int(input("Lado C: "))


def classe_de_triandulos(ladoA, ladoB, ladoC):
    if ladoA == ladoB == ladoC:
        print("O Triângulo é Equilátero!!!")
        
    elif ladoA == ladoB and ladoA != ladoC:
        print("O Triângulo é Isósceles!!!")
    else:
        print("O Triângulo é Escaleno!!!")
    return 'Os lados digitados foram', ladoA, ladoB, ladoC


print(classe_de_triandulos(ladoA, ladoB, ladoC))
