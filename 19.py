#Calculadora básica: Permite 
#operaciones básicas entre dos números

print("Calculadora basica")

while True:
    nro1 = float(input("Ingrese numero: "))
    nro2 = float(input("Ingrese numero: "))

    opcion = int(input("""
                       [1] Suma
                       [2] Resta
                       [3] Multiplicacion
                       [4] Division
                       [5] Salir : """))
    if(opcion==1):
        print(f"Suma: {nro1 + nro2}")
    elif(opcion==2):
        print(f"Resta: {nro1-nro2}")
    elif(opcion==3):
        print(f"Multiplicación: {nro1*nro2}")
    elif(opcion==4):
        print(f"Division: {nro1/nro2}")
    else:
        print("Hasta pronto!!")
        break