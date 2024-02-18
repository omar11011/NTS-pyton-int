# Dado un tiempo en segundos, diseñe un algoritmo que exprese dicho tiempo en el formato HH:MM:SS. Por ejemplo, si el tiempo es 14600 segundos, el algoritmo deberámostrar 4:3:20
import os

while True:
    os.system('cls')

    try:
        seconds = int(input("Ingresa el número de segundos: "))

        if seconds > 0:
            hours = seconds // 3600
            minutes = (seconds - hours * 3600) // 60
            seconds -= (hours * 3600 + minutes * 60)

            print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
            break
    except ValueError:
        print("Ingresa un númro válido.")