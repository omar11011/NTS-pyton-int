# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
# años que ha cumplido (desde 1 hasta su edad).
import os
os.system('cls')

while True:
    try:
        age = abs(int(input("¿Cuántos años tienes?: ")))

        if age > 0:
            for i in range(age): print(i + 1)
            break
    except ValueError:
        print("Ingresa una edad válida.")