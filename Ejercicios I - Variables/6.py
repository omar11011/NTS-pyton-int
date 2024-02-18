# Costos de los implementos por unidad
shoes = 60
shorts = 30
tShirt = 40
fullDriver = 120

while True:
    try:
        players = int(input('¿Cuántos jugadores tienes en el equipo?: '))

        if players > 0: break
    except ValueError:
        print('Ingresa un número válido de jugadores.')

initialCost = (shoes + shorts + tShirt + fullDriver) * players
discount = initialCost * 0.1
finalCost = initialCost - discount

print(f"Precio inicial: S/.{initialCost}")
print(f"Descuento del 10%: S/.{discount}")
print(f"Total a pagar: S/.{finalCost}")