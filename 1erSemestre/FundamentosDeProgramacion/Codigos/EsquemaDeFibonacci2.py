num1 = 0
num2 = 1

numero = int(input("Ingrese el n° de la repeticion del numero de Fibonacci: "))

# Validamos que el número ingresado sea mayor a 0
if numero <= 0:
    print("Por favor, ingrese un número mayor a 0.")
else:
    for i in range(numero - 1):  # Calculamos Fibonacci sin imprimir cada valor
        num1, num2 = num2, num1 + num2

    print(f"El número de Fibonacci en la posición {numero} es: {num1}")