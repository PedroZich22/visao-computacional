from PIL import Image, ImageChops

# Carregando as imagens
imagem1 = Image.open('assets/imagem1.jpg')
imagem2 = Image.open('assets/imagem2.jpg')

# Converter as imagens para modo binário (1-bit)
imagem1_bin = imagem1.convert('1')
imagem2_bin = imagem2.convert('1')

# Operação XOR
resultado_xor = ImageChops.logical_xor(imagem1_bin, imagem2_bin)
resultado_xor.show()
