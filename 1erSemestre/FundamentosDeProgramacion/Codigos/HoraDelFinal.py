hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Sumar los minutos de duración a los minutos de inicio
total_minutos = mins + dura  # Corregimos el nombre de la variable aquí

# Calcular las horas adicionales a partir de los minutos
hour += total_minutos // 60  # Añadimos las horas completas
mins = total_minutos % 60  # Calculamos los minutos restantes

# Ajustar las horas para que no superen 24 (utilizando % 24)
hour = hour % 24

# Mostrar el resultado
print(f"El evento termina a las {hour:02}:{mins:02}")
