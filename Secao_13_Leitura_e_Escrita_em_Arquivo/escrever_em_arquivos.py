"""

        Escrevendo em Arquivos

#OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

#OBS: Ao abrir um arquivo para escrita, o arquivo é criado um arquivo no sistema.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função writ()
esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caos ele já
exista, o anterior será apagado e um novo será criado. Dessa forme, todo o conteúdo no arquivo anterior
é perdido.

"""

# Exemplo de Escrita => modo 'w' vem de write(escrever) - Forma Pythônica.
with open('novo.txt', 'w') as arquivo:
    arquivo.write("Estou escrevendo em um arquivo utilizando o método with.\n")
    arquivo.write("Estou utilizando o modo 'w' que vem de write que é escrever \n")
    arquivo.write("Estou encerrando nessa linha.")


# Forma tradicional  de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer')
arquivo.write('Outro texto')

arquivo.close()

# Forma de escrever o mesmo texto multiplicado por uma variável.
with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek\n' * 1000)

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite Sair:\n ')
        if fruta != 'Sair':
            arquivo.write(f'{fruta} \n')
        else:
            break
