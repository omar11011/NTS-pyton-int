# Pedir al usuario que ingrese una cadena
while True:
    word = input("Ingresa lo que desees: ")

    if len(word) > 0: break

# Imprimir la cadena al revés
wordBackwards = word[::-1]
print(f"Lo que ingresaste al revés: {wordBackwards}")