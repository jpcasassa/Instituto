import numpy as np
import matplotlib.pyplot as plt
def metodo_A(x):
    return 0.67 * x - 12
def metodo_B(x):
    return 0.01 * x**2 - 0.4 * x + 8
#respuesta para la pregunta 1
print("El método A es lineal porque el incremento del tiempo es constante.")
print("Su modelo es: f(x) = 0.67x - 12")
x = 62
tiempo_A = metodo_A(x)
tiempo_B = metodo_B(x)
#respuesta para la pregunta 2
print(f"Método A en {x} MB: {tiempo_A:.2f} segundos")
print(f"Método B en {x} MB: {tiempo_B:.2f} segundos")

if tiempo_A < tiempo_B:
    print("→ El Método A es más rápido")
else:
    print("→ El Método B es más rápido")
# Las respuestas a la pregunta 3 son:
print("Puntos de intersección aproximados: 24 MB y 83 MB aproximadamente.")
x = np.linspace(20, 100, 200)

plt.plot(x, metodo_A(x), label="Método A", color="blue")
plt.plot(x, metodo_B(x), label="Método B", color="red")
plt.scatter(62, metodo_A(62), color="blue")
plt.scatter(62, metodo_B(62), color="red") 
plt.xlabel("Tamaño del archivo (MB)")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.show()
# La respuesta a la pregunta 4 es:
print("el metodo B es mas efectivo entre 24 MB y 83 MB, mientras que el metodo A es mas efectivo fuera de ese rango.")


