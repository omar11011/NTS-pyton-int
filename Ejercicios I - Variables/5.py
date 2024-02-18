# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

while True:
    try:
        initialCost = float(input("Ingrese el total de la compra: "))

        if initialCost > 0: break
    except ValueError:
        print("Por favor, ingrese un monto válido.")

discount = initialCost * 0.15
finalCost = initialCost - discount

print(f"Se ha realizado un descuento de S/.{discount:.2f}")
print(f"Monto final a pagar: S/.{finalCost:.2f}")