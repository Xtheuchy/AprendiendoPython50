#Polimorfismo - Sobrescribir método
#sonido en animales

#Clase padre
class Animal():
    def __init__(self, nombre):
        self.Nombre = nombre
    
    def Sonido(self):
        print("Este animal tiene un sonido")

#Clases hijas
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def Sonido(self):
        print("Guau guau")
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def Sonido(self):
        print("Miau!!")

#Creando objetos
perro = Perro("Firulais")
gato = Gato("Garfield")

#Usamos el metodo sonido
perro.Sonido()
gato.Sonido()
    