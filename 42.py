#Base de datos SQLite: Inserta
#y consulta usuarios.

import sqlite3

#1. Conexion a la base de datos
conexion = sqlite3.connect("usarios.db")

#2. Crear cursos
cursor = conexion.cursor()

#Crear tabla si no existe 
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(" \
"id INTEGER PRIMARY KEY AUTOINCREMENT," \
"nombre TEXT," \
"edad INTEGER)")

#Insertar datos a la tabla
cursor.execute("INSERT INTO usuarios(nombre,edad) VALUES (?,?)", ("Carlos",25))
cursor.execute("INSERT INTO usuarios(nombre,edad) VALUES (?,?)", ("Ana",30))
cursor.execute("INSERT INTO usuarios(nombre,edad) VALUES (?,?)", ("Luis",20))

#Guardar cambios
conexion.commit()

#Consultar todos los usuarios

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

#Mostrar resultados
print("Usuarios en la base de datos")
for usuario in usuarios:
    print(usuario)
#Cerrar conexion
conexion.close()

