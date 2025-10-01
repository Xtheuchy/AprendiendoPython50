#Contar vocales: Cuenta cuántas
#vocales tiene una frase
frase = input("Escribe una frase: ")
vocales="aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vocales:
        contador+=1
print(f"La frase tiene {contador} vocales")

