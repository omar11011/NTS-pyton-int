import os

def obtainCategory(age, title, study, work):
    if not 15 <= age <= 50:
        raise ValueError("La edad debe estar entre 15 y 50 años.")

    if 20 <= age <= 50:
        if title and work:
            return "Adulto profesionista"
        elif not work:
            return "Adulto desempleado"

    elif 15 <= age <= 20:
        if study:
            return "Joven estudiante"
        elif work and not title:
            return "Joven empleado"
        elif not study:
            return "Joven desempleado"

    return "Categoría no definida"

while True:
    os.system('cls')

    try:
        age = int(input("Ingrese la edad de la persona: "))
        title = input("¿Tiene un título? (si/no): ").lower() == "si"
        study = input("¿Está estudiando? (si/no): ").lower() == "si"
        work = input("¿Tiene trabajo? (si/no): ").lower() == "si"

        category = obtainCategory(age, title, study, work)
        print(f"La persona pertenece a la categoría: {category}")
        break
    except ValueError as e:
        print(e)