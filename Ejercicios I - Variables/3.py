# Una persona desea saber cual es su saldo bancario si el banco le paga el 2% de Interés Simple por concepto de intereses

interesRate = 0.02

while True:
    try:
        initialBalance = float(input("Ingresa tu saldo inicial: "))

        if initialBalance > 0: break 
    except ValueError:
        print("Por favor ingresa un monto válido.")

# Calcular el interés simple
simpleInterest = initialBalance * interesRate

# Calcular el saldo final
finalBalance = initialBalance + simpleInterest

# Imprimir el resultado
print(f"El interés simple es: S/.{simpleInterest:.2f}")
print(f"Tu saldo final es: S/.{finalBalance:.2f}")