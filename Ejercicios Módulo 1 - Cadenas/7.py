import os

while True:
    os.system('cls')

    try:
        phrase = input("Ingresa una frase: ")

        if len(phrase) > 0:
            phraseWithoutVowels = ''.join(character for character in phrase if character.lower() not in 'aeiouAEIOU')

            print(f"Frase sin vocales: {phraseWithoutVowels}")
            break
    except ValueError:
        print("Debes escribir algo...")