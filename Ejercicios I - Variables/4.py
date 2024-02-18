# Determine el porcentaje de varones y mujeres que hay en un salón

while True:
    try:
        numberOfMen = int(input("Ingrese la cantidad de varones en el salón: "))
        numberOfWomen = int(input("Ingrese la cantidad de mujeres en el salón: "))
        totalStudents = numberOfMen + numberOfWomen

        if numberOfMen >= 0 and numberOfWomen >= 0 and totalStudents > 0 : break
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

# Calcular el porcentaje de varones y mujeres
percentageOfMales = (numberOfMen / totalStudents) * 100
percentageOfWomen = (numberOfWomen / totalStudents) * 100

# Imprimir los resultados
print(f"Porcentaje de varones: {percentageOfMales:.2f}%")
print(f"Porcentaje de mujeres: {percentageOfWomen:.2f}%")