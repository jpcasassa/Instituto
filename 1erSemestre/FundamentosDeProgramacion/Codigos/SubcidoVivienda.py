# Listas para almacenar los datos de los postulantes
nombres = []
puntajes = []
tiene_hijos = []
tiene_contrato = []

# Variable de control
opcion = -1

# Menú
while opcion != 0:
    print("\nBienvenido a la postulación de Subsidio de Arriendo")
    print("1. Ingrese el nombre del postulante.")
    print("2. Ingrese su puntaje de Ficha de Protección Social (entre 0 y 8500).")
    print("3. ¿Tiene hijos menores de edad? (sí/no).")
    print("4. ¿Tiene contrato de trabajo vigente? (sí/no).")
    print("5. Mostrar todos los datos ingresados.")
    print("0. Salir.")
    print("Seleccione una opción:")

    try:
        opcion = int(input())
    except ValueError:
        print("Ingrese una opción numérica válida.")
        continue

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del postulante: ")
            nombres.append(nombre)
            print(f"Nombre registrado: {nombre}")
        case 2:
            try:
                puntaje = int(input("Ingrese su puntaje (0 a 8500): "))
                if 0 <= puntaje <= 8500:
                    puntajes.append(puntaje)
                    print(f"Puntaje registrado: {puntaje}")
                else:
                    print("El puntaje debe estar entre 0 y 8500.")
            except ValueError:
                print("Debe ingresar un número válido.")
        case 3:
            hijos = input("¿Tiene hijos menores de edad? (sí/no): ").lower()
            if hijos in ["sí", "si", "no"]:
                tiene_hijos.append(hijos)
                print(f"Respuesta registrada: {hijos}")
            else:
                print("Respuesta inválida. Escriba 'sí' o 'no'.")
        case 4:
            contrato = input("¿Tiene contrato de trabajo vigente? (sí/no): ").lower()
            if contrato in ["sí", "si", "no"]:
                tiene_contrato.append(contrato)
                print(f"Respuesta registrada: {contrato}")
            else:
                print("Respuesta inválida. Escriba 'sí' o 'no'.")
        case 5:
            print("\n--- Datos registrados hasta ahora ---")
            for i in range(max(len(nombres), len(puntajes), len(tiene_hijos), len(tiene_contrato))):
                print(f"\nPostulante #{i+1}")
                print("Nombre: ", nombres[i] if i < len(nombres) else "No ingresado")
                print("Puntaje: ", puntajes[i] if i < len(puntajes) else "No ingresado")
                print("Tiene hijos: ", tiene_hijos[i] if i < len(tiene_hijos) else "No ingresado")
                print("Contrato vigente: ", tiene_contrato[i] if i < len(tiene_contrato) else "No ingresado")
        case 0:
            print("Gracias por usar el sistema. ¡Hasta luego!")
        case _:
            print("Opción no válida. Intente nuevamente.")
