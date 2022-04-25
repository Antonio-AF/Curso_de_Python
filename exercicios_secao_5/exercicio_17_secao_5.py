"""

    17 - Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

    A = (basemaior + basemenor) * altura
         ---------------------------------
                    2

    Lembre-se que a base maior e a base menor devem ser maior que zero.


"""

base_bigger = float(input("Please enter a value for Base Bigger: "))
base_smaller = float(input("Please enter a value for Base Smaller: "))
height = float(input("Please enter a value for Height: "))

area = ((base_bigger + base_smaller)* height)/2

print(f'The trapezoid are is {area}')

