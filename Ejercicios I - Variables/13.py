import math

# Conversiones
inchesToCm = 2.54
feetToCm = 12 * inchesToCm

while True:
    try:
        feet = int(input("Ingresa el número de pies: "))
        inches = int(input("Ingresa el número de pulgadas: "))

        if feet >= 0 and inches > 0: break
    except ValueError:
        print("Ingresa un número válido.")

height = feet * feetToCm + inches * inchesToCm
m = int(height // 100)
cm = math.ceil(height - m * 100)

print(f"Tu altura es de aproximadamente: {m}m {cm}cm")