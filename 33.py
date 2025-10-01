#Validar número de teléfono
import re

telefono = input("Ingrese un numero de " \
"telefono (ejemplo : +51 943212543) : ")

#Expresion regular
patron = r"^\+\d{1,3}\s\d{9}$"

if(re.match(patron, telefono)):
    print("El numero de telefono es valido!!")
else:
    print("EL numero de telefono no es valido!!")
    

