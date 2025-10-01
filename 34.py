#Días hasta cumpleaños

from datetime import datetime

#pedimos al usario su fecha de cumpleaños

cumple = input("Ingrese su cumpleaños formato (mm-dd): ")

#obtener fecha actual
hoy = datetime.now()

#Fecha del proximo cumpleaño
proxCumple = datetime.strptime(f"{hoy.year}-{cumple}","%Y-%m-%d")

#Si el cumpleaños ya paso este año

if(proxCumple<hoy):
    proxCumple = datetime.strptime(f"{hoy.year+1}-{cumple}","%Y-%m-%d")

#Calculamos la diferencia en dias 
dias_faltan = (proxCumple-hoy).days

print(f"Faltan {dias_faltan} dias paraa tu cumpleaños")
