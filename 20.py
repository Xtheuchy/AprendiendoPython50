#Menú interactivo: Permite mostrar,
#agregar, eliminar elementos o salir

compras = []
while True:
    opcion = int(input("¿Qué desea realizar?" \
    "[1] Listar compras" \
    "[2] Agregar" \
    "[3] Eliminar" \
    "[4] Salir : "))
    if(opcion==1):
        n=1
        for compra in compras:
            print(f"{n} - {compra}")
            n+=1
    elif(opcion==2):
        producto = input("Que desea agregar: ")
        compras.append(producto)
        print("Producto agregado correctamente")
    elif(opcion==3):
        n=1
        for compra in compras:
            print(f"{n} - {compra}")
            n+=1
        numero = int(input("Ingrese el numero de producto a eliminar: "))
        numero-=1
        compras.pop(numero)
    elif(opcion==4):
        print("Hasta luego!!")
        break
    else:
        print("Elija una opcion valida!!")