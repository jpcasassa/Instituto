from random import randint

# Solicitar límites válidos
while True:
    try:
        inf = int(input("Límite inferior: "))
        sup = int(input("Límite superior: "))
        if inf < sup:
            break
        print("El límite inferior debe ser menor que el superior.")
    except ValueError:
        print("Por favor ingresa solo números.")

# Número aleatorio
secreto = randint(inf, sup)

# Lista para guardar intentos
intentos = []

# Bucle de 3 intentos
for i in range(3):
    intento = int(input(f"Intento {i+1}: "))
    intentos.append(intento)
    
    if intento == secreto:
        print(f"¡Felicidades! Adivinaste en el intento {i+1}.")
        break
    elif i < 2:
        print("El número es mayor." if intento < secreto else "El número es menor.")
        if i == 1:
            cercano = min(intentos, key=lambda x: abs(x - secreto))
            print(f"Pista: el número está más cerca de {cercano}.")
else:
    print("Perdiste.")
    print(f"El número era: {secreto}")
