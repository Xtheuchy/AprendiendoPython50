#Generador de pares: Usa yield

def pares_hasta(n):
    i=0
    while i<=n:
        #usamos en lugar de return
        yield i
        i+=2
#Usamos el generador con un for
for numero in pares_hasta(10):
    print(numero)