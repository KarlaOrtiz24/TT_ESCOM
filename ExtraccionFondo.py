from PIL import Image

imagen = Image.open("B.png")
imagen = imagen.convert('RGB')
maxsize = (200, 200)
imagen.thumbnail(maxsize)

def Segmentar(imagen):
    #Fondo blanco
    lower = ([50,10,0])
    high = ([235,180,170])
    #Fondo verde
    #lower = ([120,100,56])
    #high = ([255,180,150])
    imagenResultado = Image.new('1', imagen.size)
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            r,g,b = imagen.getpixel((i,j))
            if (r<lower[0] or r>high[0] and g<lower[1] or g>high[1] and b<lower[2] or b>high[2]):
                imagenResultado.putpixel((i,j),0)
            else:
                imagenResultado.putpixel((i,j),1)
    return imagenResultado

def Andimagenes(imagen, mascara):
    imagenResultado = Image.new('RGB', imagen.size)
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            pixelm = mascara.getpixel((i,j))
            pixeli = imagen.getpixel((i,j))
            if (pixelm == 1):
                imagenResultado.putpixel((i,j),pixeli)
            else:
                imagenResultado.putpixel((i,j),(0,0,0))
    return imagenResultado

mascara = Segmentar(imagen)
mascara.show()
R = Andimagenes(imagen, mascara)
R.show()
