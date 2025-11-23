#print("Dime lo que sea...")
#anything = input()
#print("Hmm...", anything, "... ¿en serio?")
#-----------------------------------------------------
# problema 3.1.6
# Usando uno de los operadores de comparación en Python, escribe un 
# programa simple de dos líneas que tome el parámetro n como entrada, 
# que es un entero, e imprime False si n es menor que 100, y True if n es 
# mayor o igual que 100.

# No debes crear ningún bloque if (hablaremos de ellos muy pronto). 
# Prueba tu código usando los datos que te proporcionamos.

#n=int(input("Ingresa un numero: "))

#print("True"if n<=100 else "False")

#--------------------------------------------------------

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numero=int(input("ingresa un numero del 1 al 1000: "))

while numero!=secret_number:
    print("!Fallaste, sigues siendo mi pricionero!.")
    numero=int(input("Intentelo de nuevo: ")) #para que el bucle continue sin errores.

print("adivinaste el numero, eres libre!")