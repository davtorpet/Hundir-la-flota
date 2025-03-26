from variables import BARCOS,TABLERO_SIZE,SIMBOLOS
import sys

class Usuario:
    USUARIOS_FILE = "usuarios.txt"
    def __init__(self):
        entrada = input("Introduce tu nombre de usuario: ")
        if entrada.lower().strip() == "exit":
            print("Saliendo del juego...Hasta la proxima!")
            sys.exit()
        self.nombre = entrada.strip()
        self.partidas_jugadas = 0
        self.flota = []


    USUARIOS_FILE = "usuarios.txt"

    # Función 1: Cargar Usuario. Desde el archivo txt y devuelve diccionario
    def cargar_usuarios(self):
        usuarios = {}
        try:
            with open(self.USUARIOS_FILE, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",") #divide por comas
                    if len(datos) == 3:
                        nombre, partidas_jugadas, partidas_ganadas = datos
                        usuarios[nombre] = {
                            "partidas_jugadas": int(partidas_jugadas),
                            "partidas_ganadas": int(partidas_ganadas)
                        }
        except FileNotFoundError:
            pass
        return usuarios

    #Función 2 guardar Usuario. Guarda en archivo txt.
    def guardar_usuarios(self,usuarios): #guardar usuarios en archivo de texto
        with open(self.USUARIOS_FILE, "w") as file:
            for nombre, datos in usuarios.items():
                file.write(f"{nombre},{datos['partidas_jugadas']},{datos['partidas_ganadas']}\n")
            

    # Función 3: Obtener Usuario. Carga usuarios existentes con cargar_usuarios().
    # Pide al usuario su nombre con input(). Si ya existe, lo saluda.
    # Si es nuevo, lo crea en el diccionario con "partidas_jugadas":0, "partidas_ganadas": 0.
    # Guarda los cambios en usuarios.json con guardar_usuarios(usuarios).
    # Retorna el nombre del usuario y el diccionario completo de usuarios.

    def obtener_usuario(self): #solicita nombre de usuario y lo registra si no existe
        usuarios = self.cargar_usuarios()
        if self.nombre in usuarios:
            print(f"¡Bienvenido de nuevo, {self.nombre}!")
        else:
            print(f"Creando nuevo usuario: {self.nombre}")
            usuarios[self.nombre] = {"partidas_jugadas": 0, "partidas_ganadas": 0}
            self.guardar_usuarios(usuarios)
        return self.nombre, usuarios

    # Función 4. Actualizar estadísticas. Carga los usuarios actuales con cargar_usuarios().
    # Si ya existe, aumenta "partudas_jugadas en +1. Si ganó (gano=True), tmb aumenta "partidas_ganadas"
    # Guarda los cambios en usuarios.json con guardar_usuarios(usuarios).

    def actualizar_estadisticas(self,nombre, gano = False): #tras una partida
        usuarios = self.cargar_usuarios()
        if nombre in usuarios:
            usuarios[nombre]["partidas_jugadas"] += 1
            if gano:
                usuarios[nombre]["partidas_ganadas"] += 1
        self.guardar_usuarios(usuarios)