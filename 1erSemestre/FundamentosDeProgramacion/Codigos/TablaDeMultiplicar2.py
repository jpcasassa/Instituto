def tabla_multiplicar(numero):
    for i in range(1, 13):  # Hasta 12
        print(f"{numero} x {i} = {numero * i}")

while True:
    # Pedir al usuario un número entero
    numero = input("Ingrese un número entero (o 'salir' para finalizar): ")
    
    if numero.lower() == 'salir':
        print("Programa finalizado.")
        break
    
    if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()):
        tabla_multiplicar(int(numero))
    else:
        print("Por favor, ingrese un número válido.")