"""

    Sistema de Arquivos - Manipulação.com


"""
import os


# Descobrindo se um arquivo ou diretório existe.
# Find out if a file or directory exist.

# Arquivos (file)
print(os.path.exists('arquivo.txt'))  # Retornou False pois não existe esse arquivo.
print(os.path.exists('arquivo.txt'))  # Return  False because the file does not exist.

print(os.path.exists('frutas.txt')) # Retorna True pois o aquivo Frutas existe.
print(os.path.exists('frutas.txt')) # Return True because the file exist.



# Diretórios (Directory)

# Paths relatives
print(os.path.exists('../Secao_12_Trabalhando_com_Módulos_Python/geek'))  # Return  True
print(os.path.exists('../Secao_12_Trabalhando_com_Módulos_Python/geek/university')) # Return True
print(os.path.exists('../Secao_12_Trabalhando_com_Módulos_Python/geek/university/geek3.py')) # Return True
print(os.path.exists('outros')) # Return False

# Path absolutes
print(os.path.exists('/home/geek/university'))
print(os.path.exists('../Secao_12_Trabalhando_com_Módulos_Python/geek/Imagens'))

# Creating files

# Form 1
open('file-test.txt', 'w').close()

# Form 2
open('file-test2.txt', 'a').close()

# Form 3
#with open('file-test3.txt', 'w') as file:
    #pass


os.mknod('file-test4.txt') # Esse comando não funciona no Windows.

