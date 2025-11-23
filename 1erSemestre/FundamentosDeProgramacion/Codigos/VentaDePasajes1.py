pasajes = 0
# Paso n° 1, solicitar la cantidad de pasajes que desea comprar

print ("¿Cuantos pasajes desea comprar?")
pasajes= int(input()) # Convertimos el texto ingresado a número entero}

for i in range (1, pasajes + 1):
    print (f"pasajes {i}: Escriba "salir" para cancelar.")

    nombre = input("Ingrese el nombre del pasajero: ")
    valor = input("Ingrese el valor del pasaje: ")
     # Verificamos si el usuario quiere salir
    if nombre.lower() == "salir":
        print("❗ Operación cancelada por el usuario.")
        break

     # Aquí podrías agregar más datos como edad, tipo de asiento, etc.
    print(f"  ✅ Valor de pasaje para {nombre} en {valor} registrado.\n")

# Paso 3: Final
print("✅ Todos los pasajes han sido registrados con éxito.")