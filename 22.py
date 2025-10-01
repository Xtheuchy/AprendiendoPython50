#Crear varios objetos y nuevos 
#métodos con la clase Persona
class Persona():

    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.Edad = edad
    
    def MostrarDatos(self):
        print(f"Mi nombre es: {self.Nombre}")
        print(f"Mi edad es: {self.Edad}")
    
    def esMayorEdad(self):
        if(self.Edad>=18):
            print("Soy mayor de edad")
        else:
            print("Soy menor de edad")

#Creando objetos
persona1 = Persona("TheUchy",20)
persona2 = Persona("Ana", 17)
persona3 = Persona("Raul", 30)

#Usamos el metodo Mostra Datos
persona1.MostrarDatos()
persona2.MostrarDatos()
persona3.MostrarDatos()

#Usamos el metodo Mayor edad
persona1.esMayorEdad()
persona2.esMayorEdad()
persona3.esMayorEdad()

