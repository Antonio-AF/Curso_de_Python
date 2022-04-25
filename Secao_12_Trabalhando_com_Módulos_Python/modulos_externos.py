"""
Módulos Externos


Utilizamos o gerenciador de pacotes Python chamado PIP - Python Installer Pachege

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama  -> É utilizado para permitir impressão de textos coloridos no terminal

# Utilizando o pacote Colorama
from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
