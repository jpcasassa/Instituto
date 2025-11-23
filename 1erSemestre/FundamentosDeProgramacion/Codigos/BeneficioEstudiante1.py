# Definición de variables iniciales
arancel = 0.0
matricula = 0.0
promedio = 0.0
quintil = 0
descuento_arancel = 0.0
descuento_matricula = 0.0
total_arancel = 0.0
total_matricula = 0.0

try:
    # Ingreso de datos
    print("Ingrese el valor total del arancel: ")
    arancel = float(input())
    print("Ingrese el valor total de la matrícula: ")
    matricula = float(input())
    print("Ingrese su promedio final: ")
    promedio = float(input())
    print("Ingrese su quintil (1 a 5): ")
    quintil = int(input())

    # Reglas para el descuento en arancel
    if promedio > 6.0:
        descuento_arancel = 0.20 if quintil in [1, 2] else 0.15 if quintil in [3, 4] else 0.0
    elif promedio > 5.0:
        descuento_arancel = 0.13 if quintil in [1, 2] else 0.10 if quintil in [3, 4] else 0.0
    else:
        descuento_arancel = 0.0

    # Reglas para el descuento en matrícula
    descuento_matricula = 0.10 if quintil in [1, 2, 3] else 0.0
    if promedio >= 5.5 and descuento_matricula > 0:
        descuento_matricula += 0.05

    # Cálculo de totales
    total_arancel = arancel * (1 - descuento_arancel)
    total_matricula = matricula * (1 - descuento_matricula)

    # Impresión de resultados
    print("\n--- Resultado ---")
    porcentaje_arancel = int(descuento_arancel * 100)
    print("Descuento arancel:", porcentaje_arancel, "%")
    porcentaje_matricula = int(descuento_matricula * 100)
    print("Descuento matrícula:", porcentaje_matricula, "%")
    print("Total a pagar por arancel: $", int(total_arancel))
    print("Total a pagar por matrícula: $", int(total_matricula))

except:
    print("Error: Ingrese solo valores numéricos válidos.")
