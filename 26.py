#Encapsulamiento - Edad privada 
#con getters y setters

class Persona():
    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.__Edad = edad
    
    #Getter : obtener
    def getEdad(self):
        return self.__Edad
    
    #Setter : Modificar
    def setEdad(self, nuevaEdad):
        if(nuevaEdad>0):
            self.__Edad = nuevaEdad
            print("Edad actualizado correctamente")
        else:
            print("Edad no valida")
    
    #Metodos propios
    def MostrarDatos(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Edad : {self.__Edad}")
#Creamos objetos
persona1 = Persona("TheUchy", 20)
persona1.MostrarDatos() #Imprime nombre y edad
print(persona1.getEdad()) #Imprimir edad
persona1.setEdad(25) #Modificar edad a 25
persona1.MostrarDatos() #Imprime nuevamente, edad = 25

persona1.Nombre = "Jorge" #Atributo no protegido (privado)

persona1.MostrarDatos()


