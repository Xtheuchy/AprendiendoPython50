#Clase Persona: Clase con nombre y edad

class persona():
    def __init__(self, nombre,edad):
        self.Nombre = nombre
        self.Edad = edad
    def MostarDatos(self):
        print(f"Mi nombre es: {self.Nombre}")
        print(f"Mi edad es: {self.Edad}")

persona1 = persona("TheUchy",20)
persona1.MostarDatos()