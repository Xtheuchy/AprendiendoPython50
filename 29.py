#Agenda de contactos - Clase 
#Contacto con lista de contactos

class Contacto():
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
    def __str__(self):
        return f"{self.nombre} - {self.numero}"

class Agenda():
    def __init__(self):
        self.contactos = []
    def agregarContacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado correctamente!!")
    def listarContactos(self):
        if not self.contactos:
            print("Lista vacia!!")
        else:
            for contacto in self.contactos : 
                print(contacto)

c1 = Contacto("Ana", "942314234")
c2 = Contacto("Roberto","921521351")

agenda = Agenda()

agenda.agregarContacto(c1)
agenda.agregarContacto(c2)

agenda.listarContactos()