idade = int(input('Qual a sua idade?'))

if idade < 12:
    print('Você é criança:')

elif (idade >= 12) and (idade <= 18):
    print('Você é adolescente:')

else:
    print("Maior de idade:")
