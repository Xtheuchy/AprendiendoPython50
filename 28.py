#Representación de objetos -
#Implementa __str__

class Persona():
    def __init__(self, nombre):
        self.Nombre = nombre

    def __str__(self):
        return f"{self.Nombre}"

persona1 = Persona("TheUchy")

print(persona1)