"""
    Modos de Abertura de Aquivos

r -> Abre para leitura - default
w -> Abre para escrita - sobrescreve caso o arquivo já exista.
x -> Abre o arquivo somente se ele não existir - caso o arquivo existe retorna o erro FileExistsError.
a -> Abre o arquivo para escrita, adicionando o conteúdo no final do arquivo.




with open('university.txt', 'x') as arquivo:
    arquivo.write("Teste de conteúdo\n")

# Teremos o erro (FileExistsError: [Error 17] File exists: 'university.txt')
"""

# Podemos tratar com o try e except para suprimir o erro.

nome_arquivo = 'university.txt'
try:
    with open(nome_arquivo, 'x') as arquivo:
        arquivo.write("Teste de Conteúdo\n")
except FileExistsError:
    print(f'O arquivo {nome_arquivo} já existe')


with open(nome_arquivo, 'a') as arquivo:
    arquivo.write("Teste de conteúdo 2\n")

with open(nome_arquivo, 'a') as arquivo:
    while True:
        fruta = input("Digite uma fruta ou sair: ")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

