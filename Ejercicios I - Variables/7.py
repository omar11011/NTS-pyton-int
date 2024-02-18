# Realizar un Programa que solicite la suma de los cuadrados de dos números, luego solicite la diferencia de los cuadrados de dichos números y finalmente muestre como respuesta cuáles eran dichos números originalmente.
import os

while True:
    os.system('cls')

    try:
        addition = int(input("Ingresa la suma de los cuadrados de dos números: "))
        subtraction = int(input("Ingresa la diferencia de los cuadrados de dos números: "))

        if addition > 0 and subtraction > 0:
            x2 = (addition + subtraction) / 2
            y2 = addition - x2
            x = x2 ** 0.5
            y = y2 ** 0.5

            print(f"Los números originales eran: {x} y {y}")

            break
    except ValueError:
        print("Ingresa dos números válidos.")