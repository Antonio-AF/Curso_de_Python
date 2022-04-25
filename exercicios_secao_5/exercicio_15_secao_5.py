"""
    15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima
    o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2
    e assim por diante.

"""

week = int(input('Please enter a number between 1 and 7: '))


def days_of_the_week(week):
    switcher = {

        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"

    }
    return switcher.get(week, "Invalid Week")


print(days_of_the_week(week))


