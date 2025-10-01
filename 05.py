#Pide edad y clasifícala en niño
#adolescente o adulto,
#Si la edad es menor que 12 → niño.
#Si la edad es menor que 18 → adolescente.
#Si no se cumple los anteriores → adulto.

edad = int(input("Ingrese su edad: "))

if(edad<12):
    print("Eres un niño")
elif(12<=edad<18):
    print("Eres un adolecente")
else:
    print("Eres un adulto")