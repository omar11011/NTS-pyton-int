# Solicite un número de celular con el prefijo del país, y devuelva el número sin el prefijo

while True:
    try:
        cellphone = input("Ingrese un número de celular con el prefijo de tu país: ")

        if "+" in cellphone and "-" in cellphone and cellphone[0] == "+":
            guionIndex = cellphone.find("-")
            code = cellphone[:guionIndex]
            number = cellphone[guionIndex + 1:]
            
            if int(code) >= 0 and int(number) > 0: break
    except ValueError:
        print("¡Ups! Parece ser que el número ingresado no tiene un prefijo.")

print(f"Código del país: {code}")
print(f"Número: {number}")