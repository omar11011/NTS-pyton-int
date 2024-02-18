import os

def obtener_signo_zodiaco(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Tauro"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Géminis"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cáncer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Escorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagitario"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricornio"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Acuario"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Piscis"
    else:
        return "Fecha no válida"

while True:
    os.system('cls')

    try:
        day = int(input("Ingrese el día de nacimiento: "))
        month = int(input("Ingrese el mes de nacimiento (en número): "))
        zodicSign = obtener_signo_zodiaco(day, month)
        print(f"El signo del zodiaco es: {zodicSign}")
        break
    except ValueError:
        print("Por favor, ingrese una fecha de nacimiento válida.")