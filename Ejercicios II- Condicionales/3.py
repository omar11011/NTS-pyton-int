import os

operations = ["+", "-", "*", "/", "^"]

while True:
    os.system('cls')

    try:
        print(f"Elige una de las siguientes operaciones:", ", ".join(operations))
        opt = input("Operación: ")

        if len(opt) > 0 and opt in operations: break
    except ValueError:
        print("El valor ingresado no es válido.")

while True:
    os.system('cls')
    print(f"Operación seleccionada: {opt}")

    try:
        result = None
        num1 = abs(int(input("Ingresa el primer número: ")))
        num2 = abs(int(input("Ingresa el segundo número: ")))

        if opt == "+": result = num1 + num2
        elif opt == "-": result = num1 - num2
        elif opt == "*": result = num1 * num2
        elif opt == "/" and num2 != 0: result = num1 / num2
        elif opt == "^": result = num1 ** num2

        if result != None:
            print(f"Resultado: {result}")
            break
    except ValueError:
        print("Por favor ingresa números enteros válidos.")