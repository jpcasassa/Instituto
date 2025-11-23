import requests

# 🔹 Reemplaza "TU_API_KEY" con la clave API que obtuviste
API_KEY = "2384a09c683a30f52fa6d4a4"
URL_BASE = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/CLP"

def convertir_divisas(pesos_clp):
    try:
        # 🔹 Hacer la solicitud a la API
        respuesta = requests.get(URL_BASE)
        datos = respuesta.json()

        # 🔹 Verificar si la solicitud fue exitosa
        if respuesta.status_code != 200:
            print("Error al obtener tasas de cambio:", datos["error-type"])
            return

        # 🔹 Obtener tasas de conversión
        tasa_usd = datos["conversion_rates"]["USD"]
        tasa_eur = datos["conversion_rates"]["EUR"]
        tasa_pen = datos["conversion_rates"]["PEN"]

        # 🔹 Realizar conversiones
        dolares = pesos_clp * tasa_usd
        euros = pesos_clp * tasa_eur
        soles = pesos_clp * tasa_pen

        # 🔹 Mostrar resultados
        print(f"\n{pesos_clp} CLP equivale a:")
        print(f"💵 {dolares:.2f} USD")
        print(f"💶 {euros:.2f} EUR")
        print(f"🇵🇪 {soles:.2f} PEN")

    except Exception as e:
        print("Error:", e)

# 🔹 Pedir cantidad en pesos chilenos
try:
    pesos = float(input("Ingrese la cantidad en pesos chilenos (CLP): "))
    if pesos < 0:
        print("Por favor, ingrese un valor positivo.")
    else:
        convertir_divisas(pesos)
except ValueError:
    print("Error: Ingrese un número válido.")