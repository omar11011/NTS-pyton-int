# Desarrollar un algoritmo para calcular la raíz cuadrada de cualquier número ingresado por teclado sea este positivo o negativo

import os

while True:
    try:
        num = float(input("Ingresa un número: "))
        break
    except ValueError:
        print("El número ingresado no es válido.")
        os.system('cls')