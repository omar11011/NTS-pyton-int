import os
import math

while True:
    os.system('cls')

    try:
        name = input("Ingresa tu nombre: ")
        
        if len(name) > 0:
            center = (len(name) + 1) / 2
            
            if len(name) % 2 > 0:
                middleLetters = name[int(center) - 1]
            else:
                center = math.floor(center)
                middleLetters = name[center - 1] + name[center]

            print(f"Nombre en mayúscula: {name.upper()}")
            print(f"Cantidad de letras: {len(name)}")
            print(f"Letras del medio: {middleLetters}")

            break
    except ValueError:
        print("Debes escribir algo...")