# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por comas.
import os
os.system('cls')

while True:
    try:
        num = abs(int(input("Ingresa un número entero positivo: ")))

        if num > 0:
            for i in range(num + 1): print(num - i)
            break
    except ValueError:
        print("Ingresa un número válido.")