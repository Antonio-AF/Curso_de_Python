# 48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundo = int(input('Digite o tempo em segundo: '))

horas = int(segundo/3600)
minutos = int(((segundo/3600)-horas)*60)
segundos = int(((((segundo/3600)-horas)*60)-minutos)*60)

print(f'Os {segundo} segundos digitados corresponde a {horas}h:{minutos}m:{segundos}s')
