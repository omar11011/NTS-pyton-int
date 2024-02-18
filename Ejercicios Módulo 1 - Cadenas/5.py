# Pedir al usuario que ingrese su nombre completo
while True:
    name = input("Ingresa tu nombre completo: ")

    if len(name) > 0: break

# Formas
print(f"Forma 1: {name.upper()}")
print(f"Forma 2: {name.title()}")