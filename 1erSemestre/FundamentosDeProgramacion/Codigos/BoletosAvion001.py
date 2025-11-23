# Declaramos las listas vacías para cada fila
fila1 = []   # Lado izquierdo - asiento A
fila2 = []   # Lado izquierdo - asiento B
fila3 = []   # Lado derecho - asiento C 
fila4 = []   # Lado derecho - asiento D

# Bucle para llenar cada lista con 40 asientos
i = 1
while i <= 40:
    # Construir el número del asiento con 2 dígitos
    if i < 10:
        # Para 1 a 9 → convierte a "01", "02", etc. usando concatenación de texto
        numero = "0" + chr(48 + i)
    else:
        # Para 10 a 40 → separa decenas y unidades, convierte a caracteres
        decenas = i // 10
        unidades = i % 10
        numero = chr(48 + decenas) + chr(48 + unidades)

    # Concatenar con la letra del asiento (A, B, C, D) y agregar a la lista
    fila1.append(numero + "A")
    fila2.append(numero + "B")
    fila3.append(numero + "C")
    fila4.append(numero + "D")

    i = i + 1  # Siguiente número de asiento

# Mostrar el avión fila por fila
j = 0
while j < 40:
    # Imprimir los 4 asientos por fila alineados
    # Se agrega un espacio después de cada asiento para mejor alineación
    print(fila1[j] + " ", fila2[j] + " ", "||", fila3[j] + " ", fila4[j])
    j = j + 1
