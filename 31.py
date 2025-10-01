#JSON básico - Guarda y lee datos
#de un archivo JSON

import json

persona = {
    "nombre":"TheUchy",
    "edad" : 20,
    "pais" : "Peru"
}

with open("persona.json","w") as archivo:
    json.dump(persona,archivo,indent=4)
    print("Guardado Exitosamente!!")

with open("persona.json", "r") as archivo:
    datos = json.load(archivo)
    print("Datos leidos!")
    print(datos)