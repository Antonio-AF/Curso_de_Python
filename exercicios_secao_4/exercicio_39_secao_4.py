# 39 - A importância de R$ 7800.000,00 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia Total:

# * O primeiro ganhador receberá 46%;
# * O segundo reeberá 32%;
# * O terceiro receberá o restante;

# Calcule e imprima a quantia ganha por cada um dos ganhadores.

premio = 780000

primeiro_lugar = float((premio * 46)/100)

#premio = premio - primeiro_lugar

segundo_lugar = float((premio * 32)/100)

terceiro_lugar = float(premio-(primeiro_lugar + segundo_lugar))

print("O Primeiro Lugar Receberá R$", primeiro_lugar)
print("O Segundo Lugar Receberá R$", segundo_lugar)
print("O Terceiro Lugar Receberá R$", terceiro_lugar)
