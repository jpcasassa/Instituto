# Paso 1: Solicitar el nombre del usuario y el saldo inicial
usuario = input("Ingrese su nombre de usuario: ")
saldo = int(input("Ingrese su saldo inicial: "))

# Paso 2: Comenzamos un bucle infinito (como el ascensor)
while True:
    print("\n=========================")
    print("Usuario:", usuario)
    print("Saldo actual: $", saldo)
    print("¿Qué desea hacer?")
    print("1. Retirar dinero")
    print("2. Salir")
    
    # Paso 3: Capturamos la opción del usuario
    opcion = input("Ingrese una opción (1 o 2): ")
    
    if opcion == "1":
        retiro = int(input("Ingrese la cantidad a retirar: "))
        
        # Paso 4: Validamos que tenga suficiente saldo
        if retiro <= saldo:
            saldo -= retiro  # Se descuenta del saldo
            print("Retiro exitoso. Nuevo saldo: $", saldo)
        else:
            print("Fondos insuficientes. Su saldo es: $", saldo)
    
    elif opcion == "2":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break  # Rompe el bucle y termina el programa
    
    else:
        print("Opción inválida. Por favor, intente de nuevo.")