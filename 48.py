#Mini servidor con FastAPI
from fastapi import FastAPI

#Creamos la aplicación 
app = FastAPI()

#Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "Hola, este es mi primer"
    "servidor con FastAPI"}
#Ruta de ejemplo
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola {nombre}, Bienvennido"}
