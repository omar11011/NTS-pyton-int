import os

opts = {
    "A": "Logro",
    "B": "En proceso",
    "C": "En proceso medio",
    "D": "En proceso inferior",
    "E": "No lo logró",
}

while True:
    os.system('cls')
    
    try:
        opt = input("Ingresa una opción: ").upper()

        if len(opt) > 0 and opt in opts:
            print(opts[opt])
            break
    except:
        print("Ingresa un dato válido.")