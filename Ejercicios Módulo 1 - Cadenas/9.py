# Pedir al usuario que ingrese una palabra
while True:
    word = input("Ingresa una palabra: ")

    if len(word) > 0: break

# Ordenar las letras de la palabra de menor a mayor
orderedWord = ''.join(sorted(word))

print(f"Palabra ordenada de menor a mayor: {orderedWord}")
