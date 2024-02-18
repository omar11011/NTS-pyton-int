# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
import os
os.system('cls')

PASSWORD = "admin1234"

while True:
    # Sensible a mayúsculas y minúsculas
    password = input("Ingresa la contraseña: ")

    if password == PASSWORD:
        print("¡Bienvenido! Te has logeado como administrador.")
        break