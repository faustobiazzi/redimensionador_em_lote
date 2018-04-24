import os , glob
try:
    from PIL import Image
except ImportError:
    import Image

    
countfile = 0
countfolder = 0
largura_desejada = 800

with open("error.txt", "w") as a:
    for path, subdirs, files in os.walk(r'.'):
       countfolder = countfolder+1
       for filename in files:
             if(".jpg" in filename) or (".JPG" in filename) or (".jpeg" in filename) or (".JPEG" in filename):
                countfile = countfile +1
            
                f = os.path.join(path, filename)
                print("trabalhando imagem "+f)
                imagem = Image.open(f)
                largura_imagem = imagem.size[0]
                if (largura_imagem > largura_desejada):
                    try:
                        altura_imagem = imagem.size[1]
                        percentual_largura = float(largura_desejada) / float(largura_imagem)
                        altura_desejada = int((altura_imagem * percentual_largura))
                        imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
                        imagem.save(f)
                        #print ("imagem " + filename + " redimensionada)
                    except Exception as ERROR:
                        a.write(str(f) + os.linesep)
                        a.write(str(ERROR) + os.linesep)
                        continue
                else:
                    continue
print ("Foram encontrados "+ str(countfile) + " Arquivos" ) 
print ("Foram encontrados "+ str(countfolder) + " Pastas" )
input ("pressione ENTER para terminar")
exit()

