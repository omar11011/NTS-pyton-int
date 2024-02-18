# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo, de altura el número introducido.
import os
os.system('cls')

while True:
    try:
        hasDividers = []
        num = abs(int(input("Ingresa un número positivo: ")))

        if num > 0:
            for i in range(num):
                if num % (i + 1) == 0: hasDividers.append(i + 1)
            
            print(f"El número {num} es primo:", "No" if len(hasDividers) > 2 else "Sí")
            break
    except ValueError:
        print("Ingresa un número válido.")