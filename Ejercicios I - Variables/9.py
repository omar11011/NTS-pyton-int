# Precios en auros
dolarPrice = 1.09
solesPrice = dolarPrice / 2.6
marcosPrice = dolarPrice / 2.12

while True:
    try:
        amountOfDolars = float(input("Ingresa la cantidad de dólares: "))
        amountOfSoles = float(input("Ingresa la cantidad de soles: "))
        amountOfMarcos = float(input("Ingresa la cantidad de marcos: "))

        if amountOfDolars > 0 and amountOfSoles > 0 and amountOfMarcos > 0: break
    except ValueError:
        print("Las cantidades a ingresar deben ser números enteros positivos.")

dolars = amountOfDolars * dolarPrice
soles = amountOfSoles * solesPrice
marcos = amountOfMarcos * marcosPrice
total = dolars + soles + marcos

print(f"El monto total en euros es de {total:.2f}")