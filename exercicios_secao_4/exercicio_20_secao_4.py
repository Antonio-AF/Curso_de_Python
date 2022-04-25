# 20 - Leia um valor de massa em quilogramas e aprsente-o convertido em libras.

# L = K/0.45

massa = float(input("Quantos kg você quer converter para Libras: "))

libras = float(massa / 0.45)

print("Para", massa, 'Kg você tem %.3f' % libras, "Libras")
