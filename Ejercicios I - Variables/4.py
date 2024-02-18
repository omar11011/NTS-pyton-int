# Determine el porcentaje de varones y mujeres que hay en un salón
import os

while True:
    os.system('cls')

    try:
        numberOfMen = abs(int(input("Ingrese la cantidad de varones en el salón: ")))
        numberOfWomen = abs(int(input("Ingrese la cantidad de mujeres en el salón: ")))
        totalStudents = numberOfMen + numberOfWomen

        if totalStudents > 0:
            percentageOfMales = (numberOfMen / totalStudents) * 100
            percentageOfWomen = (numberOfWomen / totalStudents) * 100

            print(f"Porcentaje de varones: {percentageOfMales:.2f}%")
            print(f"Porcentaje de mujeres: {percentageOfWomen:.2f}%")

        break
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")