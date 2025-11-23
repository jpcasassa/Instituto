import matplotlib.pyplot as plt

# Datos del Método A (tabla entregada)
tamano_A = [21, 40, 66, 74, 93]   # Tamaño de archivo (MB)
tiempo_A = [2.07, 14.8, 32.22, 37.58, 50.31]  # Tiempo en segundos

# Datos del Método B (función cuadrática g(x) = 0.01x^2 - 0.4x + 8)
tamano_B = list(range(20, 101, 2))  # Archivos desde 20MB hasta 100MB cada 2MB
tiempo_B = [0.01*x**2 - 0.4*x + 8 for x in tamano_B]  # Evaluamos la función

# Crear gráfico
plt.figure(figsize=(8, 5))
plt.plot(tamano_A, tiempo_A, 'ro-', label="Método A (tabla)")  # Puntos rojos
plt.plot(tamano_B, tiempo_B, 'b-', label="Método B (modelo cuadrático)")  # Línea azul

# Títulos y etiquetas
plt.title("Comparación de Tiempos de Encriptación")
plt.xlabel("Tamaño del archivo (MB)")
plt.ylabel("Tiempo de encriptación (segundos)")
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
