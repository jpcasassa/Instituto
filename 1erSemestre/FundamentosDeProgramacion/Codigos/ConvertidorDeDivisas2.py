def convertir_moneda(monto, tipo_conversion):
    # Definir las tasas de conversión
    tasas = {
        'usd': 0.055,   # Tasa de conversión de pesos a USD
        'euro': 0.051,  # Tasa de conversión de pesos a Euro
        'sol': 0.21     # Tasa de conversión de pesos a Sol
    }

    if tipo_conversion in tasas:
        return monto * tasas[tipo_conversion]
    else:
        return "Tipo de conversión no válido"

def mostrar_menu():
    print("Selecciona la moneda a la que deseas convertir:")
    print("1. De Pesos a USD")
    print("2. De Pesos a Euro")
    print("3. De Pesos a Sol")

def main():
    # Mostrar menú
    mostrar_menu()
    
    # Solicitar elección
    opcion = input("Ingresa el número de la opción que deseas: ")
    
    # Validar que la opción sea correcta
    if opcion not in ['1', '2', '3']:
        print("Opción no válida. Saliendo...")
        return
    
    # Solicitar monto en pesos
    monto = float(input("Ingresa el monto en pesos: "))
    
    # Convertir según la opción elegida
    if opcion == '1':
        resultado = convertir_moneda(monto, 'usd')
        print(f"{monto} pesos equivalen a {resultado} USD")
    elif opcion == '2':
        resultado = convertir_moneda(monto, 'euro')
        print(f"{monto} pesos equivalen a {resultado} Euros")
    elif opcion == '3':
        resultado = convertir_moneda(monto, 'sol')
        print(f"{monto} pesos equivalen a {resultado} Soles")

if __name__ == "__main__":
    main()