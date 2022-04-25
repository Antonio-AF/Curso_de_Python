# 49 - Faça um programa que leia o horário (hora, minuto e segundos) de inicio e a duração, em segundos, de uma
# experiência biológica. O programa deve resultar com o novo horário(hora, minuto e segundo) do termino da mesma.

hora_de_inicio = int(input("Digite a Hora de Inicio: "))
minuto_de_inicio = int(input("Digite os Minutos de Inicio: "))
segundo_de_inicio = int(input("Digite os Segundos de Inicio: "))
duracao_em_segundos = int(input("Digite a Duração em Segundos: "))

segundos_de_inicio = (hora_de_inicio*3600)+(minuto_de_inicio*60)+(segundo_de_inicio)
duracao = segundos_de_inicio + duracao_em_segundos

hora_final = int(duracao/3600)
minuto_final = int(((duracao/3600)-hora_final)*60)
segundo_final = int(((((duracao/3600)- hora_final)*60)-minuto_final)*60)

print(f'Hora de inicio da Experiência: {hora_de_inicio}:{minuto_de_inicio}:{segundo_de_inicio}')
print(f'A duração do expermento é de {duracao_em_segundos} Segundos')
print(f'A hora de termino do experimento é: {hora_final}:{minuto_de_inicio}:{segundo_final}')


