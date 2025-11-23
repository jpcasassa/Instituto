# Diccionario principal que guarda 3 usuarios
usuarios = {
    "17413139": {"pin": "1111", "saldo": 150000},
    "15111111": {"pin": "2222", "saldo": 500000},
    "6611111":  {"pin": "3333", "saldo": 700000}
}

# Sistema de acceso
autenticado = False  # Variable bandera para saber si el usuario ingresó correctamente

rut = input("Ingrese su RUT: ")

if rut in usuarios:
    pin = input("Ingrese su PIN: ")
    if pin == usuarios[rut]["pin"]:
        print("✅ Acceso concedido. Bienvenido al cajero automático.")
        autenticado = True
    else:
        print("❌ PIN incorrecto. Acceso denegado.")
else:
    print("❌ RUT no encontrado. Acceso denegado.")

# Solo se muestra el menú si el usuario está autenticado
if autenticado:
    while True:
        print("\n======= MENÚ DEL CAJERO AUTOMÁTICO =======")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Cambiar PIN")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            print(f"💰 Su saldo actual es: ${usuarios[rut]['saldo']}")

        elif opcion == "2":
            # Solicitar el monto a retirar
            monto_retiro = int(input("Ingrese la cantidad a retirar: $"))
            
            # Verificar si el saldo es suficiente
            if monto_retiro > usuarios[rut]['saldo']:
                print("❌ No tiene suficiente saldo para realizar el retiro.")
            else:
                # Descontar el monto del saldo
                usuarios[rut]['saldo'] -= monto_retiro
                print(f"✅ Ha retirado: ${monto_retiro}")
                print(f"💰 Su nuevo saldo es: ${usuarios[rut]['saldo']}")

        elif opcion == "3":
            # Solicitar el monto a depositar
            monto_deposito = int(input("Ingrese la cantidad a depositar: $"))

            # Validar el monto
            if monto_deposito <= 0:
                print("❌ No ha ingresado un monto correcto.")
            else:
                # Sumar el monto del depósito al saldo
                usuarios[rut]['saldo'] += monto_deposito
                print(f"✅ Ha depositado: ${monto_deposito}")
                print(f"💰 Su nuevo saldo es: ${usuarios[rut]['saldo']}")

        elif opcion == "4":
            # Paso 1: Verificar el PIN actual
            pin_actual = input("Ingrese su PIN actual: ")

            if pin_actual == usuarios[rut]['pin']:
                # Paso 2: Pedir el nuevo PIN y confirmarlo
                nuevo_pin = input("Ingrese su nuevo PIN: ")
                confirmar_pin = input("Confirme su nuevo PIN: ")

                if nuevo_pin == confirmar_pin:
                    # Paso 3: Guardar el nuevo PIN
                    usuarios[rut]['pin'] = nuevo_pin
                    print("✅ Su PIN ha sido cambiado con éxito.")
                else:
                    print("❌ Los PIN no coinciden. Intente nuevamente.")
            else:
                print("❌ El PIN actual es incorrecto.")

        elif opcion == "5":
            print("👋 ¡Gracias por usar el cajero automático!")
            break

        else:
            print("⚠️ Opción inválida. Intente nuevamente.")
