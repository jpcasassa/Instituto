# Menú simple usando diccionario
menu = {
    "cafe": 1200,
    "te": 1000,
    "jugo": 1500
}

# Mostrar el menú al usuario
print("Bienvenido a la Cafetería 🧁")
print("----- Menú -----")
for producto in menu:
    print(f"{producto.title()}: ${menu[producto]}")

# Crear lista para guardar el pedido
pedido = []

# Pedir productos al usuario
while True:
    opcion = input("\n¿Qué deseas pedir? (escribe 'salir' para terminar): ").lower()

    if opcion == "salir":
        break
    elif opcion in menu:
        pedido.append(opcion)
        print(f"{opcion} agregado al pedido.")
    else:
        print("Producto no válido. Intenta con otro.")

# Calcular el total
total = 0
for item in pedido:
    total += menu[item]

# Mostrar resumen del pedido
print("\n--- Tu pedido ---")
for item in pedido:
    print(f"- {item.title()} (${menu[item]})")

print(f"Total a pagar: ${total}")
