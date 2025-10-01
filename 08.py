#Pide números hasta que ingresen
#0, muestra la suma.

suma = 0
numero = int(input("Ingrese cero para terminar : "))

while numero!=0:
    suma += numero
    numero = int(input("Ingrese cero para terminar : "))
print(f"Suma total : {suma}")