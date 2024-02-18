import os

def convert(numero):
    if not 1 <= numero <= 99:
        raise ValueError("Por favor, ingrese un número entre 1 y 99.")

    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

    decena = numero // 10
    unidad = numero % 10

    return decenas[decena] + unidades[unidad]

while True:
    os.system('cls')

    try:
        num = int(input("Ingrese un número entre 1 y 99: "))
        result = convert(num)
        print(f"El número {num} expresado en números romanos es: {result}")
        break
    except ValueError as e:
        print(e)