import matplotlib.pyplot as plt

# Ahora las horas son reales del día: desde 6 AM hasta 20 PM
horas_reales = list(range(6, 21))  # de 6 a 20

valparaiso = []
santiago = []
concepcion = []

for h in horas_reales:
    # t es la cantidad de horas desde las 6 AM
    t = h - 6
    V = 0.9 * t**2 + 12.5 * t + 36
    S = 0.95 * t**2 + 16.8 * t + 31
    C = 1.1 * t**2 + 19.4 * t + 26
    valparaiso.append(V)
    santiago.append(S)
    concepcion.append(C)

plt.plot(horas_reales, valparaiso, label="Valparaíso")
plt.plot(horas_reales, santiago, label="Santiago")
plt.plot(horas_reales, concepcion, label="Concepción")
plt.axhline(100, color='red', linestyle='--', label="Límite 100 mm")
plt.xlabel("Hora del día")
plt.ylabel("Agua acumulada (mm)")
plt.title("Agua acumulada en 14 horas de lluvia")
plt.xticks(horas_reales)  # para que se vean todas las horas en el eje
plt.legend()
plt.grid()
plt.show()
