"""
    23 - Determine se o ano digitado é ano bissexto. Sendo que um ano é bissexto se for divisivel por 400
    ou se for divisivel por 4 e não for divisivel por 100.

"""
print("### Para saber se o ano é bissexto digite o ano abaixo###")
ano = int(input("Digite o ano: "))


def ano_bissexto(ano):
    if ano % 4 == 0 or ano % 400 == 0:
        if ano % 100 != 0:
            print(f'{ano} é Bissexto!!!')
        else:
            print(f"O ano de {ano} não é Bissexto!!!")
    else:
        print('O ano digitado não é Bissexto!!!')
    return "O ano digitado foi ", ano


ano_bissexto(ano)