#Adivinar número aleatorio: Genera
#número 1–100 y el usuario adivina
import random

nroAleatorio = random.randint(1,100)

while True:
    nroUsuario = int(input("Ingrese un numero: "))

    if(nroUsuario < nroAleatorio):
        print("Ingrese un numero mayor al anterior")
    elif(nroUsuario > nroAleatorio):
        print("Ingrese un numero menor al anterior")
    else:
        print(f"Felicidades adivinaste el numero : {nroAleatorio}")
        break
    