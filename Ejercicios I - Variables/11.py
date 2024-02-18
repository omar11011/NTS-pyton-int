# Dado un número natural de 4 cifras, diseñe un algoritmo que determine la suma y el producto de las cifras del número

while True:
    try:
        num = int(input("Ingresa un número de cuatro cifras: "))

        if num >= 1000 and num <= 9999:
            num = str(num)
            break
    except ValueError:
        print("El dato ingresado es incorrecto.")

sum = 0
prod = 1

for i in num:
    sum += int(i)
    prod *= int(i)

print(f"La suma de cifras del número {num} es {sum}")
print(f"El producto de cifras del número {num} es {prod}")