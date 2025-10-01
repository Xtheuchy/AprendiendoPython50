#Clase Coche con métodos de acción
class Coche():
    def __init__(self, marca, modelo):
        self.Marca = marca
        self.Modelo = modelo
        self.Velocidad = 0
    def Acelerar(self, cantidad):
        self.Velocidad +=cantidad
        print(f"El coche aceleró a {self.Velocidad} Km/h")
    def Frenar(self, cantidad):
        self.Velocidad-=cantidad
        if(self.Velocidad<0):
            self.Velocidad = 0
        print(f"El coche frenó a {self.Velocidad} km/h")
    def MostarDatos(self):
        print(f"Marca : {self.Marca}")
        print(f"Modelo : {self.Modelo}")
        print(f"Velocidad : {self.Velocidad} km/h")
#Creamos objetos
coche1 = Coche("Toyota","Corolla")

#Usar los metodos
coche1.Acelerar(30)
coche1.MostarDatos()
coche1.Frenar(20)
