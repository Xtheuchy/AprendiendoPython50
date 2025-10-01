#Escribir y leer archivo: Guarda
#y lee nombres en un archivo.

with open("Frutas.txt","w") as archivo:
    archivo.write("Platano\n")
    archivo.write("Manzana\n")
    archivo.write("Pera\n")
with open("Frutas.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)