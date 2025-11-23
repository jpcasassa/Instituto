# Variables base
valor_arancel = 0
valor_matricula = 0

# Entrada de datos
try:
    promedio = float(input("Ingrese su promedio: "))
    quintil = int(input("Ingrese su quintil (1, 2, 3, 4 o 5): "))

    if quintil not in [1, 2, 3, 4, 5]:
        print("El quintil ingresado no es válido. Debe ser un número del 1 al 5.")
    elif promedio < 1.0 or promedio > 7.0:
        print("El promedio debe estar entre 1.0 y 7.0.")
    else:
        # Inicializamos los descuentos
        descuento_arancel = 0
        descuento_matricula = 0
        beneficios = []

        # Cálculo descuento en arancel
        if promedio > 6.0:
            if quintil in [1, 2]:
                descuento_arancel = 0.20
                beneficios.append("20% de descuento en arancel")
            elif quintil in [3, 4]:
                descuento_arancel = 0.15
                beneficios.append("15% de descuento en arancel")
        elif 5.0 < promedio <= 6.0:
            if quintil in [1, 2]:
                descuento_arancel = 0.13
                beneficios.append("13% de descuento en arancel")
            elif quintil in [3, 4]:
                descuento_arancel = 0.10
                beneficios.append("10% de descuento en arancel")
        
        # Cálculo descuento en matrícula
        if quintil in [1, 2, 3]:
            descuento_matricula = 0.10
            beneficios.append("10% de descuento en matrícula")
            if promedio >= 5.5:
                descuento_matricula += 0.05
                beneficios.append("5% adicional en matrícula por promedio ≥ 5.5")

        # Aplicar descuentos
        valor_final_arancel = int(valor_arancel * (1 - descuento_arancel))
        valor_final_matricula = int(valor_matricula * (1 - descuento_matricula))

        # Mostrar resultados
        print("\nBeneficios obtenidos:")
        if beneficios:
            for b in beneficios:
                print(f"- {b}")
        else:
            print("- No tiene beneficios aplicables.")

        print(f"\nValor final del arancel: ${valor_final_arancel}")
        print(f"Valor final de la matrícula: ${valor_final_matricula}")

except ValueError:
    print("Error: Ingrese valores numéricos válidos. Use punto (.) para los decimales.")
