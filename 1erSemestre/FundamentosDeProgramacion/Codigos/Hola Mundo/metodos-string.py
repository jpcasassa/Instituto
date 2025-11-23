animal = "       peRriTo Feliz"
print(animal.upper())         # Convierte todo el texto a MAYÚSCULAS
print(animal.lower())         # Convierte todo el texto a minúsculas
print(animal.strip().capitalize())  # Elimina espacios y pone la primera letra en mayúscula, el resto en minúscula
print(animal.title())         # Convierte la primera letra de cada palabra en mayúscula
print(animal.strip())         # Elimina los espacios en blanco al inicio y final del texto
print(animal.lstrip())        # Elimina solo los espacios en blanco de la izquierda (inicio del texto)
print(animal.rstrip())        # Elimina solo los espacios en blanco de la derecha (final del texto)
print(animal.find("ri"))      # Devuelve el índice donde empieza "ri" o -1 si no lo encuentra
print(animal.replace("peRr", "cierv")) # Reemplaza "peRr" por "cierv" en el texto
print("peRri" in animal)      # Devuelve True si "peRri" está dentro de animal, si no, False
print("peRri" not in animal)  # Devuelve True si "peRri" NO está dentro de animal, si no, False
