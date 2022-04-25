

s = float(input('Digite um expoente valido: '))
n = int(input('Digite um numero inteiro: '))

n_interaction = n
z_list = []
i = 0
z = 0

# Efetua as operações para casa inteiro e adiciona na lista.
while i <= n_interaction:
    if n > 0:
        z = 1/n**s
        n = n - 1
        i = i + 1
        z_list.append(z)
    else:
        print('Divisão por zero')
        break

print(z)
print(z_list)

# Laço for responsavel por somar os resultados de z da lista
soma_z = 0
for z in z_list:
    soma_z += z

print(f' A soma de todos os Z é {soma_z}')