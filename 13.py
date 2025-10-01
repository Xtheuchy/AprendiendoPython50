#Función que saluda, usa 'invitado' 
#si no recibe nombre.

def saludar(nombre="invitado"):
    print(f"Hola {nombre}")

#Con nombre
saludar("Ana")

#Sin nombre
saludar()
