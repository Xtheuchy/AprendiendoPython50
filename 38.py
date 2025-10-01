#Leer CSV con pandas: Muestra primeras filas
import pandas as pd

#Leemos el archivo csv
df = pd.read_csv("ventas.csv")

#Mostramos las primeras filas
print(df.head(3))