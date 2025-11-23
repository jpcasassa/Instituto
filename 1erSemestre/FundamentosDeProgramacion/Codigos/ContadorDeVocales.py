def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for letra in palabra:
        if letra in vocales:
            contador += 1
    
    return contador

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Contar vocales
total_vocales = contar_vocales(palabra)

# Mostrar resultado
print(f"La palabra '{palabra}' tiene {total_vocales} vocal(es).")