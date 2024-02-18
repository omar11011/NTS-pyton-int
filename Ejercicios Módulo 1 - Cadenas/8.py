while True:
    try:
        estatura_metros = float(input("Ingresa tu estatura en metros con dos decimales: "))

        if 0 < estatura_metros: break
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")

# Extraer la parte entera y la parte decimal
parte_entera = int(estatura_metros)
parte_decimal_centimetros = round((estatura_metros - parte_entera) * 100)

# Imprimir el resultado
print(f"{parte_entera} metros y {parte_decimal_centimetros} centímetros.")