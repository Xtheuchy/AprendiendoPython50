#Crear carpetas: Genera carpetas automáticamente.

import os

carpetas = ["Documentos","Videos","Musica","Imagenes"]

for carpeta in carpetas:
    os.makedirs(carpeta,exist_ok=True)
    print(f"Carpeta creada correctamente : {carpeta}")