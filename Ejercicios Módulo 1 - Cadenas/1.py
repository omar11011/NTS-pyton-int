import os

while True:
    os.system('cls')
    
    try:
        word = input('Escribe algo: ')
        repetitions = abs(int(input('Indica el número de veces a repetir: ')))

        if len(word) > 0 and repetitions > 0:
            print(' '.join([word] * repetitions))
            break
    except:
        print('Por favor, ingresa un número entero válido.')