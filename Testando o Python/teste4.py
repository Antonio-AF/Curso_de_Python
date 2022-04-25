'''from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)

print(f'A data de hoje é {now.day}/{now.month}/{now.year} e são {now.hour}Horas')'''

from datetime import date

data_atual = date.today()

if data_atual.month == 0o6:
    print('A data de hoje é: ', data_atual)

else:
    print('Erro')

from datetime import datetime

print(data_atual)

now = datetime.now()

print(now.day)

print(type(now.day))