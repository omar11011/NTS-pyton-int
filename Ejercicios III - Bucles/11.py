# Escriba un programa que solicite una contraseña (el texto de la contraseña no es
# importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
import os
os.system('cls')

while True:
    password = input("Ingresa una contraseña: ")

    if len(password) > 0: break

print("¡Ups! Parece que alguien más ha ingresado antes con tu contraseña, por seguridad vuelve a escribirla.")

attemps = 3

while attemps > 0:
    passwordConfirm = input("Ingresa tu contraseña para verificar: ")

    if password == passwordConfirm:
        print("Ok, parece que sí eres tú. He enviado a tu correo un link para cambiar tu contraseña.")
        break
    else: attemps -= 1

if attemps < 1: print("Se ha bloqueado tu cuenta temporalmente. Comunícate con el soporte.")