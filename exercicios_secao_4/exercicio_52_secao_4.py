# 52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente
# ao valor que cada d um deu para a realização da aposta. Faça um programa que leia quanto cada apostador
# Investiu, o valor prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

premio = int(input('Digite de uanto é o premio em que foi apostado: R$'))

joao = int(input('Digite quanto João investiu: R$'))
pedro = int(input('Digite quato Pedro investiu: R$'))
maria = int(input('Digite quanto Maria investiu: R$'))

total = joao + pedro + maria

porc_joao = float((joao * 100)/total)
porc_pedro = float((pedro * 100)/total)
porc_maria = float((maria * 100)/total)

premio_joao = float((premio * porc_joao)/100)
premio_pedro = float((premio * porc_pedro)/100)
premio_maria = float((premio * porc_maria)/100)


print('O Premio que João ira Ganhar é R$%.2f'%premio_joao)
print('O Premio que Pedro irá Ganhar é R$%.2f'%premio_pedro)
print('O Premio que Maria irá Ganhar é de R$%.2f'%premio_maria)
