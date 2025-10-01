#Pide un número entero y clasifícalo.
#Número positivo, negativo o cero.

numero = int(input("Ingrese un numero: "))

if(numero>0):
    print("El numero es positivo")
elif(numero<0):
    print("El numero es negativo")
else:
    print("El numero es cero.")
