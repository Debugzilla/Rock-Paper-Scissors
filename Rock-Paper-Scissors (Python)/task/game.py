import random

# Opciones estándar y extra
opciones_estandar = ["rock", "paper", "scissors"]
opciones_extra = ["rock", "paper", "scissors", "lizard", "spock"]

puntos = 0  # Variable global para el puntaje


def obtener_opcion_usuario():
    global puntos  # Aseguramos que puntos sea la variable global
    name = input("Enter your name: ")
    print(f"Hello, {name}")

    # Intentamos leer el archivo para cargar el puntaje del usuario
    try:
        with open("rating.txt", "r") as archivo:
            for linea in archivo:
                nombre, puntos_str = linea.strip().split()
                if nombre.lower() == name.lower():
                    puntos = int(puntos_str)  # Convertir puntos a entero
                    break
    except FileNotFoundError:
        print("Rating file not found.")

    # Opciones personalizadas de juego
    entrada = input().lower()
    if not entrada:
        print("Okay, let's start")
        return opciones_estandar  # Opción 1: estándar si no se introduce nada
    else:
        opciones_usuario = [opcion.strip() for opcion in entrada.split(",")]
        if set(opciones_usuario) == set(opciones_estandar):
            print("Okay, let's start")
            return opciones_estandar
        elif set(opciones_usuario) == set(opciones_extra):
            print("Okay, let's start")
            return opciones_extra
        else:
            print("Okay, let's start")
            return opciones_usuario  # Opción personalizada


def salir():
    print("Bye!")
    exit(0)  # Salir completamente del programa


def jugar(opciones):
    global puntos
    while True:
        jugador = input().lower()

        # Opción especial para mostrar el puntaje actual
        if jugador == "!rating":
            print(f"Your rating: {puntos}")
            continue  # Regresa al inicio del loop sin salir

        # Opción especial para salir del programa
        if jugador == "!exit":
            salir()  # Llama a la función salir para manejar la salida

        # Verificar que la opción sea válida
        if jugador not in opciones:
            print("Invalid input.")
            continue  # Regresa al inicio del loop sin salir

        # Opción de la computadora
        computadora = random.choice(opciones)
        # print(f"Tú elegiste: {jugador}")
        # print(f"La computadora eligió: {computadora}")

        # Determinar el resultado
        if jugador == computadora:
            print(f"There is a draw ({computadora})")
            puntos += 50  # Sumar puntos por empate
        elif (jugador, computadora) in reglas_juego(opciones):
            print(f"Well done. The computer chose {computadora} and failed.")
            puntos += 100  # Sumar puntos por victoria
        else:
            print(f"Sorry, but the computer chose {computadora}.")


def reglas_juego(opciones):
    if opciones == opciones_estandar:
        return {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
    elif opciones == opciones_extra:
        return {
            ("rock", "scissors"), ("rock", "lizard"),
            ("scissors", "paper"), ("scissors", "rock"),
            ("paper", "rock"), ("paper", "spock"),
            ("lizard", "spock"), ("lizard", "paper"),
            ("spock", "scissors"), ("spock", "lizard")
        }
    elif opciones == opciones:
        return {
            ("fire","snake"), ("fire","human"),("fire","tree"),("fire","wolf"),("fire","sponge"),("fire","scissors"),
            ("rock", "scissors"), ("rock", "snake"), ("rock", "fire"), ("rock", "human"), ("rock", "tree"),("rock","wolf"),("rock","sponge"),
            ("gun","fire"),("gun","rock"),("gun","scissors"),("gun","wolf"),("gun","tree"),
            ("lightning","gun"),("lightning","rock"),("lightning","fire"),("lightning","scissors"),("lightning","human"),("lightning","snake"),("lightning","tree"),
            ("devil","lightning"),("devil","gun"),("devil","rock"),("devil","fire"),("devil","scissors"),("devil","snake"),("devil","human"),
            ("dragon","devil"),("dragon","lightning"),("dragon","gun"),("dragon","rock"),("dragon","fire"),("dragon","scissors"),("dragon","snake"),
            ("water","dragon"),("water","devil"),("water","lightning"),("water","gun"),("water","rock"),("water","fire"),("water","scissors"),
            ("air","water"),("air","dragon"),("air","devil"),("air","lightning"),("air","gun"),("air","rock"),("air","fire"),
            ("paper","air"),("paper","water"),("paper","dragon"),("paper","devil"),("paper","lightning"),("paper","gun"),("paper","rock"),
            ("sponge","paper"),("sponge","air"),("sponge","water"),("sponge","dragon"),("sponge","devil"),("sponge","lightning"),("sponge","gun"),
            ("wolf","sponge"),("wolf","paper"),("wolf","air"),("wolf","air"),("wolf","water"),("wolf","dragon"),("wolf","devil"),("wolf","lightning"),
            ("tree","wolf"),("tree","sponge"),("tree","paper"),("tree","air"),("tree","water"),("tree","devil"),
            ("human","tree"),("human","wolf"),("human","sponge"),("human","paper"),("human","air"),("human","water"),("human","dragon"),
            ("snake","human"),("snake","tree"),("snake","wolf"),("snake","sponge"),("snake","paper"),("snake","air"),("snake","water"),
            ("scissors","snake"),("scissors","human"),("scissors","tree"),("scissors","wolf"),("scissors","sponge"),("scissors","paper"),("scissors","air")





        }



def guardar_puntuacion(name, puntos):
    # Guardar la puntuación en el archivo
    with open("rating.txt", "a") as archivo:
        archivo.write(f"{name} {puntos}\n")


# Inicio del programa
opciones = obtener_opcion_usuario()
jugar(opciones)
guardar_puntuacion(opciones, puntos)