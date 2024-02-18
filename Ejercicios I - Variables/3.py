# Una persona desea saber cual es su saldo bancario si el banco le paga el 2% de Interés Simple por concepto de intereses
import os

while True:
    os.system('cls')

    try:
        interesRate = 0.02
        initialBalance = float(input("Ingresa tu saldo inicial: "))
        simpleInterest = initialBalance * interesRate
        finalBalance = initialBalance + simpleInterest

        print(f"El interés simple es: S/.{simpleInterest:.2f}")
        print(f"Tu saldo final es: S/.{finalBalance:.2f}")

        break 
    except ValueError:
        print("Por favor ingresa un monto válido.")