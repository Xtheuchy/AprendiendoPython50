#Método estático - Devuelve año actual
from datetime import datetime

class Utilidades():
    @staticmethod
    def obtenerAñoActual():
        return datetime.now().year

print(f"El año actual es : {Utilidades.obtenerAñoActual()}")
    