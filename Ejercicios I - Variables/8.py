# Diseñe un programa que lea un número entero de cinco cifras y determine la cifra central del número. Por ejemplo, si el número ingresado fuera 34217, la cifra central a mostrar es 2

while True:
    try:
        num = int(input("Ingresa un número de cinco cifras: "))

        if num >= 10000 and num <= 99999:
            num = str(num)
            break
    except ValueError:
        print("El dato ingresado es incorrecto.")

print(f"La cifra del centro del número proporcionado es {num[2]}")