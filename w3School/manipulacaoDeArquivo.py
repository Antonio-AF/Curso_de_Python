
# A função Open() serve para manipular aquivos de texto ou binário.


#f = open("texto.txt", "xt")

import os

f = open("texto.txt", "r")
for x in f:
    print(x)

f.close()

os.remove("texto.txt")