word = input('Escribe algo: ')

# Validamos que el número de veces pueda convertirse a entero positivo
while True:
    try:
        repetitions = int(input('Indica el número de veces a repetir: '))

        if repetitions > 0: break
        else : print('Por favor, ingresa un número válido.')
    except:
        print('Por favor, ingresa un número entero válido.')

# Convertimos a array para multiplicarlo y separarlo por espacio
print(' '.join([word] * repetitions))