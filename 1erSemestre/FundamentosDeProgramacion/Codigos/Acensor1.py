print("Bienvenido Ascensor")
print("Usted esta en el Piso: ")
print("Seleccione Piso")
mipiso = int(input())
piso= 0

#bloque de proceso
print ("Este ascensor esta SUBIENDO | BAJANDO")

print("Bienvenido al Ascensor")  # Mensaje de bienvenida

# Inicializar variables
piso = 0  # El ascensor comienza en el piso 0
print("Usted esta en el Piso:", piso)  # Mostrar piso actual

# Solicitar al usuario que seleccione el piso
print("Seleccione el piso al que desea ir (1-5):")
opcion = int(input())  # El usuario selecciona el piso

# Bloque de proceso
if opcion > piso:  # Si el piso seleccionado es mayor que el actual, el ascensor sube
    print("Este ascensor esta SUBIENDO")  
    for i in range(piso, opcion + 1):  # Subiendo piso por piso
        print("Subiendo al Piso:", i)
elif opcion < piso:  # Si el piso seleccionado es menor que el actual, el ascensor baja
    print("Este ascensor esta BAJANDO")  
    for i in range(piso, opcion - 1, -1):  # Bajando piso por piso
        print("Bajando al Piso:", i)
else:
    print("Ya esta en el Piso", piso)  # Si el usuario selecciona el piso actual

# Al final, actualizar el piso del ascensor al destino elegido 1
piso = opcion
print("Usted ha llegado al Piso:", piso)  # Mostrar el piso final