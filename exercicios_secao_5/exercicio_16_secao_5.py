"""

    16 - Usando o switch, faça um programa que leia um numero inteiro entre 1 e 12
    e imprima o mês correspondente a este numero. Isto é, Janeiro se 1, e assim por
    diante.


"""

month = int(input('Please enter a number between 1 and 12: '))


def month_of_the_year(month):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(month, "Invalid Month")


print(month_of_the_year(month))
