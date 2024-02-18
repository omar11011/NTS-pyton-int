import math

name = input("Ingresa tu nombre: ")
center = (len(name) + 1) / 2

if len(name) % 2 > 0:
    middleLetters = name[int(center) - 1]
else:
    center = math.floor(center)
    middleLetters = name[center - 1] + name[center]

print(f"Nombre en mayúscula: {name.upper()}")
print(f"Cantidad de letras: {len(name)}")
print(f"Letras del medio: {middleLetters}")