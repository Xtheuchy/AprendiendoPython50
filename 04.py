#Pide nombre y edad. Muestra 
#la edad dentro de 10 años
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

edad_Futura = edad + 10

print(f"Hola {nombre}, tu edad dentro",
      f"de 10 años será: {edad_Futura}")
