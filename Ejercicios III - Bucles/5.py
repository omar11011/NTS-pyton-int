# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por comas.
import os
os.system('cls')

while True:
    try:
        num = abs(int(input("Ingresa un número entero positivo: ")))

        if num > 0:
            if num % 2 == 1: num += 1
            numbers = list(range(1, num, 2))
            print(", ".join(map(str, numbers)))
            break
    except:
        print("Error")