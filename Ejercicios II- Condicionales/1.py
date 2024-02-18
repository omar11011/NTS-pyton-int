# Escriba un programa que solicite el ingreso de un número y verifique si es numero divisible por 3 o es divisible por 7.

import os

while True:
    try:
        num = float(input("Ingresa un número: "))
        mult3 = num % 3 == 0
        mult7 = num % 7 == 0

        print(f"Divisible por 3: ", "Si" if mult3 else "No")
        print(f"Divisible por 7: ", "Si" if mult7 else "No")

        break
    except ValueError:
        print("Ingresa un número válido.")
        os.system('cls')