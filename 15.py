#División con manejo de error:
#Maneja división por cero.
try:
    a = float(input("Ingrese un numero : "))
    b = float(input("Ingrese un numero : "))
    resultado = a / b
    print("Resultado: ", resultado)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
    