#Herencia básica - Clase 
#Estudiante que hereda de Persona

#Clase padre
class Persona():
    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.Edad = edad
    def MostrarDatos(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Edad : {self.Edad}")

#Clase hija
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.Carrera = carrera
    def MostrarCarrera(self):
        print(f"Carrera : {self.Carrera}")

#Creamos objetos
estudiante1 = Estudiante("Jorge",35,"Arquitecto")
estudiante1.MostrarDatos()
estudiante1.MostrarCarrera()