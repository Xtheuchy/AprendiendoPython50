#Gráfico de barras: Muestra
#ventas de productos.

import matplotlib.pyplot as plt

#datos de ejemplo

productos = ["Laptop","Mouse","Teclado",
             "Monitor","Audifonos"]

ventas = [25,40,30,15,20]

#Crear grafico de barras
plt.bar(productos, ventas, color="skyblue")

#Titulo y etiquetas
plt.title("Ventas de productos")
plt.xlabel("Productos")
plt.ylabel("Cantidad Vendida")

#Mostrar grafico
plt.show()