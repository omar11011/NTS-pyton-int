# Escriba un programa que pregunte una y otra vez si desea continuar con el programa,
# siempre que se conteste exactamente sí (en minúsculas y con tilde).
import os
os.system('cls')

while True:
    opt = input("¿Deseas continuar con el programa? (sí/no): ")

    if opt == "sí":
        print("El programa se ha cerrado.")
        break