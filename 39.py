#Analizador de texto: Cuenta líneas,
#palabras y caracteres

#Abrir un archivo de texto en modo lectura
with open("texto.txt","r", encoding="utf-8") as texto:
    contenido = texto.read()
with open("texto.txt","r", encoding="utf-8") as texto:
    lineas = texto.readlines()

cantidad_lineas = len(lineas)
cantidad_palabras = len(contenido.split())
cantidad_caracteres = len(contenido)

print(f"Lineas : {cantidad_lineas}")
print(f"Palabras : {cantidad_palabras}")
print(f"Caracteres : {cantidad_caracteres}")
