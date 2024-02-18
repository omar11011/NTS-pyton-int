# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
import os
os.system('cls')

while True:
    try:
        word = input("Ingresa una palabra: ")
        
        if len(word) > 0:
            for i in range(10): print(word)
            break
    except ValueError:
        print("Debes ingresar una palabra.")