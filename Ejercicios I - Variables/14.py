basicSalary = 300
discountPercentage = 11
commissionPercentage = 9

while True:
    try:
        sales = float(input("¿Cuánto vendiste este mes?: "))

        if sales >= 0: break
    except ValueError:
        print("Inserta un monto válido.")

commission = sales * commissionPercentage / 100
grossSalary = basicSalary + commission
discount = grossSalary * discountPercentage / 100
netIncome = grossSalary - discount

print(f"Sueldo bruto: S/.{grossSalary}")
print(f"Descuento: S/.{discount}")
print(f"Sueldo neto: S/.{netIncome}")