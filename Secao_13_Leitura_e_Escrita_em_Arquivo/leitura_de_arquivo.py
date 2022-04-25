'''

                ###Leitura em Arquivo###

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de
entreda, que neste caso é o caminho do arquivos a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o aquivo para leitura. Este arquivo
deve xexistir, ou então teremos o erro FileNotFoundError

mode r -> Modo de Leitura. r-> read() -> Do inglês ler.

'''

# Exemplo

arquivo = open('texto.txt')


print(arquivo)

print(type(arquivo))

# para ler o conteúdo de um arquivo, após sua abertura,
# devemos utilizar a função read()

print(arquivo.read())

# Obs: O Python, utiliza um recusro para trabalhar com arquivos chamado cursor.
# Esse cursor, funciona como o cursor quando estamos escrevendo.


# Obs: A função read() lê todo o conteúdo do arquivo.