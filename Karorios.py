print ("Hello, this a my project with Pillow ")
# Esta es una prueba de el trabajo en entorno virtual, estoy usando la libreria Pillow con la cual se pueden crear imagenes.
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def crear_imagen():
    # Crear una nueva imagen en blanco
    img = Image.new("RGB", (500, 300), color=(255, 255, 255))
    
    # Dibujar un rectángulo y texto
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, 50, 450, 250], outline="blue", width=5)
    draw.text((150, 130), "Hola, Pillow!", fill="red")
    
    # Aplicar un filtro de desenfoque
    img_blur = img.filter(ImageFilter.BLUR)
    
    # Guardar las imágenes
    img.save("imagen_creada.jpg")
    img_blur.save("imagen_desenfocada.jpg")
    
    # Mostrar las imágenes
    img.show()
    img_blur.show()
    
    print("Imagen creada y guardada correctamente.")

crear_imagen()
