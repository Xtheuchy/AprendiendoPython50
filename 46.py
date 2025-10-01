# Día 46: Multithreading básico
import threading
import time

def tarea1():
    for i in range(5):
        print(f"Tarea 1 → paso {i+1}")
        #simulamos que tarda 1 segundo
        time.sleep(1)
def tarea2():
    for i in range(5):
        print(f"Tarea 2 → paso {i+1}")
        #simulamos que tarda 1 segundo
        time.sleep(1)

#Creamos 2 hilos (threads)

hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)

#Iniciamos los 2 hilos
hilo1.start()
hilo2.start()

#Esperamos a que terminen
hilo1.join()    
hilo2.join()

print("Ambas tareas terminaron!")