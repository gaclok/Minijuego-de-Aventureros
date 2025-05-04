# Diccionarios de personajes (aventureros)
personajes = {
    "Guerrero": {"vida": (100, 100), "ataque": (15, 20), "defensa": (10, 15)},
    "Mago": {"vida": (80, 80), "ataque": (20, 25), "defensa": (5, 10)},
    "Arquero": {"vida": (90, 90), "ataque": (18, 22), "defensa": (8, 12)}
}

# Lista de nombres de personajes para selección
lista_personajes = list(personajes.keys())

import random

# Jugador elige personaje
print("Elige tu personaje:")
for i, nombre in enumerate(lista_personajes, 1):
    print(f"{i}. {nombre}")

opcion = int(input("Número: ")) - 1
jugador = lista_personajes[opcion]
stats_jugador = personajes[jugador]

# Máquina elige personaje aleatorio (excluyendo al jugador)
oponente = random.choice([p for p in lista_personajes if p != jugador])
stats_oponente = personajes[oponente]

print(f"\n¡{jugador} vs {oponente}!\n")

# Acciones posibles (lista)
acciones = ["atacar", "defender"]

while True:
    # Turno del jugador
    print(f"Turno de {jugador} (Vida: {stats_jugador['vida'][0]})")
    print("1. Atacar\n2. Defender")
    accion_jugador = acciones[int(input("Elige acción (1/2): ")) - 1]

    # Turno de la máquina (aleatorio)
    accion_oponente = random.choice(acciones)
    print(f"\n{oponente} elige {accion_oponente}.\n")

    # Resolución de turno
    if accion_jugador == "atacar":
        danio = random.randint(*stats_jugador["ataque"])  # Ataque aleatorio dentro del rango
        if accion_oponente == "defender":
            danio -= random.randint(*stats_oponente["defensa"])
            danio = max(0, danio)  # No permitir daño negativo
        stats_oponente["vida"] = (stats_oponente["vida"][0] - danio, stats_oponente["vida"][1])
        print(f"{jugador} ataca a {oponente} por {danio} de daño.")

    if accion_oponente == "atacar" and accion_jugador != "defender":
        danio = random.randint(*stats_oponente["ataque"])
        stats_jugador["vida"] = (stats_jugador["vida"][0] - danio, stats_jugador["vida"][1])
        print(f"{oponente} ataca a {jugador} por {danio} de daño.")

    # Verificar si alguien murió
    if stats_jugador["vida"][0] <= 0:
        print(f"\n¡{oponente} gana!")
        break
    if stats_oponente["vida"][0] <= 0:
        print(f"\n¡{jugador} gana!")
        break

    print("----------------------")
    
while True:
    try:
        opcion = int(input("Número: ")) - 1
        if 0 <= opcion < len(lista_personajes):
            break
    except ValueError:
        print("¡Ingresa un número válido!")
print("\n--- Resumen del Combate ---")
print(f"{jugador}: Vida restante = {max(0, stats_jugador['vida'][0])}")
print(f"{oponente}: Vida restante = {max(0, stats_oponente['vida'][0])}")
