# Datos de usuario
numBase = int(input("Ingrese un número base: "))
numExpo = int(input("Ingrese un exponente: "))

# Cualquier número elevado a 0 es 1
numTotal = 1

# Si el exponente es mayor que 0, multiplicamos
if numExpo > 0:
    for i in range(numExpo):
        numTotal = numTotal * numBase

# Si el exponente es 0, el resultado es 1 (ya está inicializado como 1)

# Si el exponente es negativo, mostramos un mensaje (opcional)
elif numExpo < 0:
    print("Este programa no maneja exponentes negativos.")
    numTotal = "no definido"

# Mostrar resultado si es válido
if numTotal != "no definido":
    print("El número", numBase, "elevado a", numExpo, "es:", numTotal)
