"""

        Sistema de Arquivos e Navegação

Para fazer o uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do
módulo OS.

os -> Operating System - Sistema Operacional

"""
import os

# getcwd() -> Pega o Current Work Directory - Diretório de Trabalho Corrente
# Retorna o Path ou seja retorna o caminho absoluto.
diretorio = os.getcwd()
print(f'O Diretório corrente é {diretorio}')

# Podemos mudar de diretorio usando o chdir().
os.chdir('..')
diretorio_atual = os.getcwd()
print(f'Esse é o diretorio atual {diretorio_atual}')

# Podemos checar se um diretorio é absoluto ou relativo.
# No Windows utilizamos duas barras para diferenciar do caracter  \
print(os.path.isabs('C:\\Users\\Antonio'))

# Caso precisamos verificar em que sitema operacional estamos rodando nosso program,
# utilizamos o seguinte comando.
print(os.name)
# Para sistemas linux e Mac o nome do sistema será Posix
# Já para sistemas Windows o nome será NT

# Podemos ter mais detalhes do sistema operacional.
'''print(os.uname())''' # Somente para Linux

# '/home/geek/workspace/sistema'

print(os.getcwd())  #C:\Users\Antonio\Documents\PycharmProjects\guppe

res = os.path.join(os.getcwd(), 'geek', 'university')
# Podemos juntar nomes de diretórios (Pastas) com o caminho especificado por os.getcwd()

os.chdir(res)

print(os.getcwd()) #C:\Users\Antonio\Documents\PycharmProjects\guppe\geek\university

# Podemos listar os aquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)

print(arquivos)

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, da mesma forma quando abrirmos um arquivo.

scanner.close()