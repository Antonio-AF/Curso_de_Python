"""
    String IO

Atenção: Para ler ou escrever dados em arquivos dos sistema operacional o software precisa ter permissão.
    - Permissão de Leitura -> Para ler arquivos.
    - Permissão de Escrita -> Para escrever o arquivos.


StringIo -> Utilizado para ler e criar arquivos em memória.


"""

# Primeiro passo para utilizar a função StringIo precisamos importa-lo.
from io import StringIO

mensagem = "Esta é uma string normal"

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazia para inserirmos texto depois

arquivo = StringIO(mensagem)
# Isso é a mesma coisa que escrever arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo podemos utilizar tudo o que já sabemos.
print(arquivo.read())

# Escrevendo outros textos.
arquivo.write(' Testando as funcionalidades da função StringIo')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())

