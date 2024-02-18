import os

while True:
    os.system('cls')

    try:
        estatura_metros = abs(float(input("Ingresa tu estatura en metros con dos decimales: ")))

        if estatura_metros > 0:
            parte_entera = int(estatura_metros)
            parte_decimal_centimetros = round((estatura_metros - parte_entera) * 100)

            print(f"{parte_entera} metros y {parte_decimal_centimetros} centímetros.")          
            break
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")