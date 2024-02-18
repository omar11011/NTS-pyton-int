# Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario anterior.

while True:
    try:
        oldSalary = float(input("Ingresa tu salario anterior: "))

        if oldSalary > 0: break
    except ValueError:
        print("Por favor, ingresa un monto válido.")

# Calcular el nuevo salario con un incremento del 25%
increase = 25
newSalary = oldSalary * (100 + increase) / 100

# Imprimir el resultado
print(f"Tu nuevo salario con un incremento del {increase}% es: S/.{newSalary:.2f}")