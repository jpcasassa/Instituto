# Diccionario con usuarios y contraseñas
usuarios = {
    "pedro": "1234",
    "angel": "a4s1"
}

# Solicitar datos al usuario
userid = input("Ingrese su nombre de usuario: ")
contrasenaid = input("Ingrese su contraseña: ")

# Validación
if userid in usuarios:
    if usuarios[userid] == contrasenaid:
        print("Acceso concedido. ¡Bienvenido,", userid + "!")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no encontrado.")

try:
    # Solicitar las tres notas
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    # Calcular el promedio
    promedio = (nota1 + nota2 + nota3) / 3

    # Mostrar el promedio
    print(f"El promedio es: {promedio:.1f}")

    # Verificar si está aprobado
    if promedio >= 4.0:
        print("Aprobado")
    else:
        print("Reprobado")
except ValueError:
    print("Error: Debe ingresar solo valores numéricos.")