# vibra.py

import json
import random

class Usuario:
    def _init_(self, nombre, edad, intereses):
        self.nombre = nombre
        self.edad = edad
        self.intereses = intereses
        self.likes = set()

    def dar_like(self, otro_usuario):
        """Dar like a otro usuario"""
        self.likes.add(otro_usuario.nombre)
        print(f"{self.nombre} le dio like a {otro_usuario.nombre}")

    def hizo_match(self, otro_usuario):
        """Revisa si hay match mutuo"""
        return self.nombre in otro_usuario.likes and otro_usuario.nombre in self.likes


def recomendar(usuario, lista_usuarios):
    """Recomienda un usuario aleatorio que no sea el mismo"""
    candidatos = [u for u in lista_usuarios if u.nombre != usuario.nombre]
    return random.choice(candidatos) if candidatos else None


def guardar_usuarios(usuarios, archivo="usuarios.json"):
    """Guarda lista de usuarios en archivo JSON"""
    data = []
    for u in usuarios:
        data.append({
            "nombre": u.nombre,
            "edad": u.edad,
            "intereses": u.intereses,
            "likes": list(u.likes)
        })
    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)


def cargar_usuarios(archivo="usuarios.json"):
    """Carga lista de usuarios desde archivo JSON"""
    try:
        with open(archivo, "r") as f:
            data = json.load(f)
        usuarios = []
        for u in data:
            nuevo = Usuario(u["nombre"], u["edad"], u["intereses"])
            nuevo.likes = set(u["likes"])
            usuarios.append(nuevo)
        return usuarios
    except FileNotFoundError:
        return []


# ------------------- DEMO -------------------

if _name_ == "_main_":
    # Crear algunos usuarios
    juan = Usuario("Juan", 25, ["música", "cine", "fútbol"])
    maria = Usuario("María", 23, ["arte", "música", "viajes"])
    alessandro = Usuario("Alessandro", 28, ["viajes", "tecnología", "deporte"])
    claudio = Usuario("Claudio", 27, ["fútbol", "cine", "tecnología"])
    martin = Usuario("Martín", 26, ["arte", "lectura", "gaming"])

    usuarios = [juan, maria, alessandro, claudio, martin]

    # Likes y matches
    juan.dar_like(maria)
    maria.dar_like(juan)

    if juan.hizo_match(maria):
        print("🔥 ¡Match encontrado entre Juan y María!")
    else:
        print("Todavía no hay match...")

    # Recomendación
    recomendado = recomendar(juan, usuarios)
    print(f"👉 {juan.nombre}, te recomendamos conocer a {recomendado.nombre}")

    # Guardar usuarios
    guardar_usuarios(usuarios)

    # Cargar usuarios desde archivo
    usuarios_cargados = cargar_usuarios()
    print("\n📂 Usuarios cargados desde JSON:")
    for u in usuarios_cargados:
        print("-", u.nombre, u.edad, u.intereses, "Likes:", u.likes)