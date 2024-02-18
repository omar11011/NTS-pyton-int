import os
import math

# Conversiones
inchesToCm = 2.54
feetToCm = 12 * inchesToCm

while True:
    os.system('cls')

    try:
        feet = abs(int(input("Ingresa el número de pies: ")))
        inches = abs(int(input("Ingresa el número de pulgadas: ")))

        if feet >= 0 and inches > 0:
            height = feet * feetToCm + inches * inchesToCm
            m = int(height // 100)
            cm = math.ceil(height - m * 100)

            print(f"Tu altura es de aproximadamente: {m}m {cm}cm")
            break
    except ValueError:
        print("Ingresa un número válido.")