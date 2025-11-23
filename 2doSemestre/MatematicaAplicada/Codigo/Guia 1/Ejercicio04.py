# Ejemplo: Cálculo y gráfico de agua acumulada en distintas ciudades
# Curso: Matemática Aplicada
# Nivel: Primer año de Ingeniería en Informática
# --------------------------------------------

import matplotlib.pyplot as plt  # Librería para gráficos

# ------------------------------------------------------
# Pregunta 1:
# Calcular el agua acumulada en Concepción a las 07:30 AM
# ------------------------------------------------------

# Definimos el tiempo t como horas transcurridas desde las 6:00 AM
t = 1.5  # 07:30 AM está a 1.5 horas después de las 6:00 AM

# Fórmula dada para el agua acumulada en Concepción (en mm)
C = 1.1 * t**2 + 19.4 * t + 26

print("A las 07:30 AM, en Concepción hay", round(C, 2), "mm de agua acumulada.")


# ------------------------------------------------------
# Pregunta 2:
# Graficar la evolución del agua acumulada en Valparaíso,
# Santiago y Concepción durante 14 horas de lluvia
# ------------------------------------------------------

# Usamos horas reales del día: desde las 6 AM hasta las 20 PM
horas_reales = list(range(6, 21))  # [6, 7, 8, ..., 20]

# Listas vacías donde guardaremos los resultados de cada ciudad
valparaiso = []
santiago = []
concepcion = []

# Recorremos cada hora real del día
for h in horas_reales:
    # t es el tiempo contado desde las 6 AM
    t = h - 6

    # Fórmulas dadas para cada ciudad
    V = 0.9 * t**2 + 12.5 * t + 36
    S = 0.95 * t**2 + 16.8 * t + 31
    C = 1.1 * t**2 + 19.4 * t + 26

    # Guardamos los resultados en las listas
    valparaiso.append(V)
    santiago.append(S)
    concepcion.append(C)

# Dibujamos los gráficos
plt.plot(horas_reales, valparaiso, label="Valparaíso")
plt.plot(horas_reales, santiago, label="Santiago")
plt.plot(horas_reales, concepcion, label="Concepción")

# Línea horizontal que marca el límite de 100 mm
plt.axhline(100, color='red', linestyle='--', label="Límite 100 mm")

# Etiquetas y título
plt.xlabel("Hora del día")
plt.ylabel("Agua acumulada (mm)")
plt.title("Agua acumulada en 14 horas de lluvia")

# Mostrar todas las horas en el eje X
plt.xticks(horas_reales)

# Mostrar leyenda y cuadrícula
plt.legend()
plt.grid()
plt.show()


# ------------------------------------------------------
# Pregunta 3:
# Determinar la primera ciudad que supera los 100 mm
# ------------------------------------------------------

for t in range(15):  # de 0 a 14 horas después de las 6 AM
    V = 0.9 * t**2 + 12.5 * t + 36
    if V > 100:
        print("Valparaíso supera los 100 mm a las", 6 + t, "horas")
        break

for t in range(15):
    S = 0.95 * t**2 + 16.8 * t + 31
    if S > 100:
        print("Santiago supera los 100 mm a las", 6 + t, "horas")
        break

for t in range(15):
    C = 1.1 * t**2 + 19.4 * t + 26
    if C > 100:
        print("Concepción supera los 100 mm a las", 6 + t, "horas")
        break


# ------------------------------------------------------
# Pregunta 4:
# Calcular cuánta agua cayó entre las 3 y 5 de la tarde
# ------------------------------------------------------

# Recordemos: 3 PM son 9 horas después de las 6 AM
t_inicio = 9   # 3 PM
t_fin = 11     # 5 PM

# Calculamos el agua acumulada en cada ciudad al inicio y al final
V_inicio = 0.9 * t_inicio**2 + 12.5 * t***_*_
