# Imaginemos que queremos saber la velocidad que has alcanzado durante un viaje.

distancia = 0 
tiempo = 0
velocidad = 0
opcion = 0

while True:
    print("\n¿Tuviste un viaje? ¿Qué quieres saber?")
    print("1) Distancia promedio")
    print("2) Tiempo promedio")
    print("3) Velocidad promedio")
    print("0) Salir")
    
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("⚠️ Error: Debes ingresar un número. Inténtalo de nuevo.")
        continue

    if opcion == 1:  # calculando la 
        try:
            print("Ingrese el tiempo y la velocidad promedio")
            tiempo = float(input("Ingrese el tiempo promedio (en horas): "))
            velocidad = float(input("Ingrese la velocidad promedio (en km/h): "))
            if tiempo <= 0 or velocidad <= 0:
                print("⚠️ Error: El tiempo y la velocidad deben ser mayores que cero.")
                continue
            distancia = velocidad * tiempo
            print(f"La distancia promedio fue de: {distancia} km")
        except ValueError:
            print("⚠️ Error: Debes ingresar números válidos.")

    elif opcion == 2:  # calculando el tiempo
        try:
            print("Ingrese la distancia y la velocidad promedio")
            distancia = float(input("Ingresa la distancia promedio (en km): "))
            velocidad = float(input("Ingresa la velocidad promedio (en km/h): "))
            if velocidad <= 0:
                print("⚠️ Error: La velocidad debe ser mayor que cero.")
                continue
            tiempo = distancia / velocidad
            print(f"El tiempo promedio fue de: {tiempo} horas")
        except ValueError:
            print("⚠️ Error: Debes ingresar números válidos.")

    elif opcion == 3:  # calculando la velocidad
        try:
            print("Ingrese la distancia y el tiempo promedio")
            distancia = float(input("Ingresa la distancia promedio (en km): "))
            tiempo = float(input("Ingrese el tiempo promedio (en horas): "))
            if tiempo <= 0:
                print("⚠️ Error: El tiempo debe ser mayor que cero.")
                continue
            velocidad = distancia / tiempo
            print(f"La velocidad promedio fue de: {velocidad} km/h")
        except ValueError:
            print("⚠️ Error: Debes ingresar números válidos.")

    elif opcion == 0:
        print("¡Hasta luego! 👋")
        break

    else:
        print("⚠️ Opción no válida. Elige una opción del 0 al 3.")
distancia