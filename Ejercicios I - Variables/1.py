# Determinar el área de un triángulo rectángulo
import os

while True:
    os.system('cls')

    try:
        c1 = abs(float(input("Ingresa el valor del primer cateto: ")))
        c2 = abs(float(input("Ingresa el valor del segundo cateto: ")))
        
        if c1 > 0 and c2 > 0:
            area = c1 * c2 / 2

            print(f'El área de un triángulo con catetos {c1} y {c2} es aproximadamente {area:.2f}')
            break
    except:
        print('Ingresa los datos correctamente.')