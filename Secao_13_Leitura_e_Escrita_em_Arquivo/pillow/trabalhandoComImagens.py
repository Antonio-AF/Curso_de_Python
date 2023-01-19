from PIL import Image
import glob
import os

# print(im.format, im.size, im.mode)  # Comando nos dá o tamanho da imagem a extensão e o sistema de cor.

# im.show() # Metodo para printar a imagem.

im = Image.open("usina.jpg")

print(im.format, im.size, im.mode)

# Reduzindo o tamenho da imagem
size = 228, 228

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", "JPEG")

im.show()
