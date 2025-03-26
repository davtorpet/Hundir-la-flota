# INTEGRARLO EN MAIN:
from Tablero import *
from variables import *
from Usuario import Usuario
import time

if __name__ == "__main__":

    print("Hundir a la flota! Vamos a jugar")
    print("Introduce los datos de tu cuenta:")
    print("*"*40)
    
    jugador_usuario = Usuario()
    nombre_usuario, usuarios = jugador_usuario.obtener_usuario()

    print("A JUGAR!!")
   
    # Creamos los tableros
    jugador = Tablero()
    maquina = Tablero()

    print("Posicionando tu barcos aleatoriamente...")
    time.sleep(1)
    tab1 = jugador.posicionar_barco_aleatorio()
    print("Posicionando los barcos de la máquina aleatoriamente...")
    time.sleep(1)
    tab2 = maquina.posicionar_barco_aleatorio(ocultar_barcos=True)
    print("Tu tablero:\t\t\tTablero de la máquina:")
    jugador.mostrar_tableros_lado_a_lado(tab1,tab2)

    turno_jugador = True
    while True: 
        if turno_jugador:
            print("*"*50,"\nTU TURNO!\n")
            print("Mostrando tus tableros...")
            time.sleep(2)
            tab1 = jugador.mostrar_tablero(jugador.tablero)
            tab2 = jugador.mostrar_disparos_realizados()
            print("Tu tablero:\t\t\tTablero de disparos:")
            jugador.mostrar_tableros_lado_a_lado(tab1,tab2)
            
            disparo = jugador.disparo_jugador(maquina.tablero)

            while disparo == SIMBOLOS["IMPACTO"]:
                disparo = jugador.disparo_jugador(maquina.tablero)
            turno_jugador = False

            if jugador.verificar_victoria(maquina.tablero) == True:
                print("FIN DE LA PARTIDA")
                jugador_usuario.actualizar_estadisticas(nombre_usuario, gano = True)
                break
        else:
            print("*"*50,"\nTURNO DE LA MAQUINA")
            time.sleep(2)
            disparo = maquina.disparo_maquina(jugador.tablero)
            while disparo == SIMBOLOS["IMPACTO"]:
                disparo = maquina.disparo_maquina(jugador.tablero)
            turno_jugador = True
            time.sleep(2)
            if maquina.verificar_victoria(jugador.tablero) == True:
                print(f"La máquina ha ganado. Suerte la próxima vez, {nombre_usuario}.")
                print("FIN DE LA PARTIDA")
                jugador_usuario.actualizar_estadisticas(nombre_usuario,gano=False)
                break


            