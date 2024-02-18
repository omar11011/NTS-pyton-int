# Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario anterior.
import os

while True:
    os.system('cls')
    
    try:
        oldSalary = float(input("Ingresa tu salario anterior: "))
        increase = 25
        newSalary = oldSalary * (100 + increase) / 100

        print(f"Tu nuevo salario con un incremento del {increase}% es: S/.{newSalary:.2f}")

        break
    except ValueError:
        print("Por favor, ingresa un monto válido.")