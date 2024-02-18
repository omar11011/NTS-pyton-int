# Determinar el área de un triángulo rectángulo

print('¡Bienvenid@ a tu calculadora de área de un triángulo rectángulo!')
print('Por favor ingresa los catetos separados por espacios.')

while True:
    try:
        cathetos = input('Catetos: ')
        cathetos = [abs(int(num)) for num in cathetos.split()]
        
        if (len(cathetos) > 1 and cathetos[0] > 0 and cathetos[1] > 0):
            area = cathetos[0] * cathetos[1] / 2
            area = "{:.2f}".format(area)

            print(f'El área de un triángulo con catetos {cathetos[0]} y {cathetos[1]} es aproximadamente {area}')
            break
    except:
        print('Ingresa los datos correctamente.')