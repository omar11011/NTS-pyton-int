# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo, de altura el número introducido.
import os
os.system('cls')

while True:
    try:
        num = abs(int(input("Ingresa un número entero positivo: ")))

        if num > 0:
            for i in range(num): print("*" * (i + 1))
            break
    except ValueError:
        print("Ingresa un número válido.")