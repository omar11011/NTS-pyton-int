import os

while True:
    os.system('cls')

    try:
        name = input("Ingresa tu nombre completo: ")

        if len(name) > 0:
            print(f"Forma 1: {name.upper()}")
            print(f"Forma 2: {name.title()}")
            break
    except ValueError:
        print("Debes escribir algo...")