import os

def convert(numero):
    unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    especiales = ['', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']

    # Validar que el número esté en el rango
    if not 0 <= numero <= 99:
        raise ValueError("Por favor, ingrese un número entre 0 y 99.")

    # Convertir el número a letras
    if numero == 0:
        return "cero"
    elif 1 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return especiales[numero - 10]
    else:
        decena = numero // 10
        unidad = numero % 10

        if unidad == 0: return decenas[decena]
        else: return decenas[decena] + " y " + unidades[unidad]

while True:
    os.system('cls')

    try:
        num = int(input("Ingrese un número entre 0 y 99: "))
        result = convert(num)
        print(f"El número {num} expresado en letras es: {result}")
        break 
    except ValueError as e:
        print(e)