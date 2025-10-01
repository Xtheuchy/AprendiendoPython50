#convierte texto a voz
import pyttsx3

engine = pyttsx3.init()

texto = input("Escribe un texto: ")

engine.say(texto)

engine.runAndWait()