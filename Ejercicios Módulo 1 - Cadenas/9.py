import os

while True:
    os.system('cls')

    try:
        word = input("Ingresa una palabra: ")

        if len(word) > 0:
            orderedWord = ''.join(sorted(word))

            print(f"Palabra ordenada de menor a mayor: {orderedWord}")
            break
    except ValueError:
        print("Debes escribir algo...")