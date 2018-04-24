import sys
import os
try:
    from PIL import Image
except ImportError:
    import Image



files_dir = "."
print (files_dir)
arquivo = [f for f in os.listdir(files_dir) if f.endswith("JPG")]
largura_desejada = 800
        
for filename in arquivo:
    print("trabalhando imagem "+filename)
    imagem = Image.open(files_dir+"/"+filename)
    largura_imagem = imagem.size[0]
    altura_imagem = imagem.size[1]
    percentual_largura = float(largura_desejada) / float(largura_imagem)
    altura_desejada = int((altura_imagem * percentual_largura))

    imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
    imagem.save(filename)
   
