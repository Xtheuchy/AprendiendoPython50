#Reporte de datos: Procesa CSV y guarda resumen.

import pandas as pd

#Leemos el archivo
df = pd.read_csv("ventas.csv")

#Mostras las primeras filas
print(df.head(3))

#Procesar datos
print("\n resumen estadistico")
print(df.describe())

#Guardamos el resumen en un nuevo
#archivo 

resumen = df.describe()

resumen.to_csv("resumen_ventas.csv",index=True)

print("Se ha guardado el resumen")