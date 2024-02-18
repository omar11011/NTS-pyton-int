# Desarrollar un algoritmo para calcular la raíz cuadrada de cualquier número ingresado por teclado sea este positivo o negativo
import os

while True:
    os.system('cls')

    try:
        num = float(input("Ingresa un número: "))
        r = abs(num) ** 0.5

        # Constante imaginaria i = (-1)**0.5 para las raíces de los números negativos
        if num < 0: r = f"{r}i"

        print(f"La raíz cuadrada de {num} es {r}")
        break
    except ValueError:
        print("El número ingresado no es válido.")