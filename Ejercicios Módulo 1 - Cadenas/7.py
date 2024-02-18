# Pedir al usuario que ingrese una frase
while True:
    phrase = input("Ingresa una frase: ")

    if len(phrase) > 0: break

# Eliminar todas las vocales
phraseWithoutVowels = ''.join(character for character in phrase if character.lower() not in 'aeiouAEIOU')

# Imprimir el resultado
print(f"Frase sin vocales: {phraseWithoutVowels}")