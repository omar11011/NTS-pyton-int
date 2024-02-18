import os

# Conversiones
toMegaBytes = 1024
toKiloBytes = toMegaBytes ** 2
toBytes = toMegaBytes ** 3

while True:
    os.system('cls')
    
    try:
        num = abs(float(input("Ingresa el número de GigaBytes: ")))

        if num > 0:
            print(f"MegaBytes: {num * toMegaBytes}")
            print(f"KiloBytes: {num * toKiloBytes}")
            print(f"Bytes: {num * toBytes}")

            break
    except ValueError:
        print("Ingresa un número válido.")