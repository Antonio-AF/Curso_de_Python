import scipy.integrate as integrate
import scipy.special as special


exp = int(input("Digite um Expoente: "))
num = int(input("Digite um Número: "))


def soma(a, b):
    result_soma = a + b
    return result_soma


def exponential():
    num3 = soma(num, exp)
    result = pow(num, num3)
    return result


print(exponential())


result = integrate.quad(lambda x: special.jv(3.5, x), 0, 4.5)
print(result)
