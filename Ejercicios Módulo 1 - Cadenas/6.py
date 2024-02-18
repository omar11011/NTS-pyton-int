import os

while True:
    os.system('cls')
    
    try:
        word = input("Ingresa lo que desees: ")

        if len(word) > 0:
            wordBackwards = word[::-1]

            print(f"Lo que ingresaste al revés: {wordBackwards}")
            break
    except ValueError:
        print("Debes escribir algo...")