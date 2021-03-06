#!/usr/bin/python
# coding: UTF-8

import cgi, os, sys
import cgitb; cgitb.enable()

formatted = True

# Lista de arquivos que não podem ser vistos pelo usuário
privados = ['fetch_page.py']

# Criamos uma função para verificar se dois arquivos se
# correspondem
def samefile(path1, path2):
    apath1 = os.path.abspath(path1).lower()
    apath2 = os.path.abspath(path2).lower()
    return apath1 == apath2

# Criamos o texto html da página
html = """
<html><title>Minha Pagina</title>
<h1>Codigo fonte para: '%s'</h1>
<hr>
<pre>%s</pre>
<hr></html>"""


# Criamos a função restrita para verificar se o arquivo
# solicitado coincide com um dos arquivos considerados
# como restritos
def restrito(filename):
    for path in privados:
        if samefile(path, filename):
            return True

# Criamos também uma função para achar qualquer arquivo
# dentro do servidor
def acha_arquivo(arquivo):
    for root, dirs, files in os.walk(os.getcwd()):
        for nome in files:
            if nome == arquivo: 
                return os.path.join(root, nome)
    return 'Arquivo não Encontrado!'

# Tentamos obter o nome do arquivo a ser baixado por
# meio do formulário para esse script, se esse script
# tiver sido executado sem essas informações o arquivo
# a ser baixado é o download.py
try:
    form = cgi.FieldStorage()
    filename = form['filename'].value
except:
    filename = 'download.py'

# Fazemos com que não possa ser aberto um arquivo de
# acesso restrito, além disso se o arquivo não existir
# nós também colocamos na tela uma mensagem de erro adequado
if restrito(filename):
    filetext = '(Acesso não permitido)'
else:
    caminho = acha_arquivo(filename)
    if caminho != 'Arquivo não Encontrado!':
       filetext = open(caminho).read()
    else:
       filetext = '(Erro ao abrir arquivo: %s)' % filename

# Por fim imprimimos a criamos a tela de HTML
if not formatted:
    print('Content-type: text/plain\n')
    print(filetext)
else:
    print('Content-type: text/html\n')
    print(html % (filename, cgi.escape(filetext)))
