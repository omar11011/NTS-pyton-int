# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
import os

while True:
    os.system('cls')
    
    try:
        initialCost = abs(float(input("Ingrese el total de la compra: ")))
        discount = initialCost * 0.15
        finalCost = initialCost - discount

        print(f"Se ha realizado un descuento de S/.{discount:.2f}")
        print(f"Monto final a pagar: S/.{finalCost:.2f}")

        break
    except ValueError:
        print("Por favor, ingrese un monto válido.")