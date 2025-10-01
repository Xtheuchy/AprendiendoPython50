#Decorador de tiempo: Mide tiempo de ejecución

#Importamos el modulo time
import time

def medir_tiempo(funcion):
    def wrapper():
        #Guardamos el tiempo antes de ejecutar
        inicio = time.time()
        funcion()
        #Guardamos el tiempo despues de ejecutar
        fin = time.time()
        print("Tiempo de ejecucion", fin - inicio, "segundos")
    return wrapper
#Aplicamos el decorador 
@medir_tiempo
def tarea_lenta():
    #El bucle tarda en terminar
    for i in range(1000000):
        pass
tarea_lenta()