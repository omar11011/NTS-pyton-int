import os

basicSalary = 300
discountPercentage = 11
commissionPercentage = 9

while True:
    os.system('cls')

    try:
        sales = float(input("¿Cuánto vendiste este mes?: "))

        if sales >= 0:
            commission = sales * commissionPercentage / 100
            grossSalary = basicSalary + commission
            discount = grossSalary * discountPercentage / 100
            netIncome = grossSalary - discount

            print(f"Sueldo bruto: S/.{grossSalary}")
            print(f"Descuento: S/.{discount}")
            print(f"Sueldo neto: S/.{netIncome}")

            break
    except ValueError:
        print("Inserta un monto válido.")