# Metodo de tablero
import numpy as np
from variables import BARCOS, TABLERO_SIZE, SIMBOLOS
import time
import sys

class Tablero():
    flota = {"B0" : 1,"B1" : 1,"B2" : 1,"B3" : 1, "B4" : 2,"B5" : 2,"B6" : 2, "B7" : 3,"B8" : 3,"B9" : 4 }
    def __init__(self):
        self.tablero = np.full((TABLERO_SIZE, TABLERO_SIZE), " ")
        self.disparos_realizados = np.full((TABLERO_SIZE, TABLERO_SIZE), " " )

#La matriz self.disparos_realizados debe coincidir con TABLERO_SIZE en lugar de ir fijada a 10x10

#Llena la matriz con el símbolo de agua ("-") definido en SIMBOLOS["AGUA"].


    def posicionar_barco_aleatorio(self,ocultar_barcos=False):
        TableroAuxiliar = self.tablero.copy()
        for indice,valor in self.flota.items():
            ubicado =  0 
            Colision_Detectada = 0
            
            # Creamos arrays random para Posicion Inicial y Orientacion Inicial.
            while ubicado == 0:

                Posicion_Inicial = np.random.randint(0,TABLERO_SIZE,size=2)
                Orientacion_Inicial = np.random.choice(["N","S","E","O"])
                Tamaño_Barco = valor
                # Si detectamos colision recuperamos el tablero inicial
                if Colision_Detectada == 0:
                    TableroAuxiliarSafe = TableroAuxiliar.copy()
                
                elif Colision_Detectada == 1:
                    TableroAuxiliar = TableroAuxiliarSafe.copy()
                    Colision_Detectada = 0
                
                # Condiciones ubicacion limite
                FueraNorte = Orientacion_Inicial == "N" and Posicion_Inicial[0] - Tamaño_Barco < 0
                FueraSur = Orientacion_Inicial == "S" and Posicion_Inicial[0] + Tamaño_Barco > 10
                FueraEste = Orientacion_Inicial == "E" and Posicion_Inicial[1] + Tamaño_Barco > 10
                FueraOeste = Orientacion_Inicial == "O" and Posicion_Inicial[1] - Tamaño_Barco < 0
                # Condiciones de direccion
                RecorroFila = Orientacion_Inicial == "N" or Orientacion_Inicial == "S" 
                RecorroColumna = Orientacion_Inicial == "E" or Orientacion_Inicial == "O" 
                Sentido = 1
                if Orientacion_Inicial == "O" or Orientacion_Inicial == "N" :
                    Sentido = -1            
                # Comprobamos ubicaciones limite
                if FueraNorte == False and FueraSur == False and FueraEste == False and FueraOeste == False:
                    # Comprobamos y pintamos
                    for i in range(Tamaño_Barco):
                        if TableroAuxiliar[Posicion_Inicial[0] + i*Sentido*RecorroFila, Posicion_Inicial[1] + i*Sentido*RecorroColumna] == SIMBOLOS["BARCO"]:
                            Colision_Detectada = 1
                            break
                        else:
                            TableroAuxiliar[Posicion_Inicial[0] + i*Sentido*RecorroFila ,Posicion_Inicial[1] + i*Sentido*RecorroColumna] = SIMBOLOS["BARCO"]#indice[1]
                            
                    if Colision_Detectada == 0:
                        ubicado = 1                                                                            
        self.tablero = TableroAuxiliar.copy()
        return self.mostrar_tablero(self.tablero,ocultar_barcos)

    def mostrar_tablero(self,tablero,ocultar_barcos = False):
        tablero_copy = tablero.copy()
        if ocultar_barcos:
            tablero_copy[tablero_copy == SIMBOLOS["BARCO"]] = " "
  
        # Imprimir encabezado de columnas
        # Objetivo: Imprimir cada fila del tablero, agregando el índice de la fila al inicio.
        lineas=[]
        encabezado = "   " + " ".join(str(i+1) for i in range(TABLERO_SIZE))
        lineas.append(encabezado)
        for i, fila in enumerate(tablero_copy):
            linea = f"{i+1:2} " + " ".join(fila)
            lineas.append(linea)
        return lineas

    def mostrar_disparos_realizados (self):
        tablero_copy = self.disparos_realizados.copy()
        # Imprimir encabezado de columnas
        # Objetivo: Imprimir cada fila del tablero, agregando el índice de la fila al inicio.
        lineas=[]
        encabezado = "   " + " ".join(str(i+1) for i in range(TABLERO_SIZE))
        lineas.append(encabezado)
        for i, fila in enumerate(tablero_copy):
            linea = f"{i+1:2} " + " ".join(fila)
            lineas.append(linea)
        return lineas
            
    
    def introducir_coordenadas(self):
        print("Introduce las coordenadas que quieras entre el 1 y 10")
        valido = False
        while not valido:
            entrada = input("Dame coordX y coordY separados por coma ").strip()
            if entrada.lower() == "exit":
                print("Saliendo del juego...Hasta la proxima!")
                sys.exit()
            try:
                cor_X,cor_Y = map(int,entrada.split(","))
                cor_X -= 1
                cor_Y -= 1
                if (cor_X in range(TABLERO_SIZE)) & (cor_Y in range(TABLERO_SIZE)):
                    valido = True
                else:
                    print("Coordenadas fuera del tablero.Prueba de nuevo")
            except ValueError:
                print("Error: ingresa un número por favor")
        return cor_X,cor_Y


    def comprobar_disparo_jugador(self,coordX,coordY,tablero):
        if tablero[coordX,coordY] == " ":
            disparo = SIMBOLOS["AGUA"]
            print("Ha tocado agua :(")
        elif tablero[coordX,coordY] == SIMBOLOS["BARCO"]:
            disparo = SIMBOLOS["IMPACTO"]
            print("Bien hecho, le has tocado a un barco!!")
        elif (tablero[coordX,coordY] == SIMBOLOS["IMPACTO"]) or (tablero[coordX,coordY] == SIMBOLOS["AGUA"]):
            print("Ya has disparado en esas coordenadas,prueba de nuevo")
            cordX,cordY = map(int,input("Dame coordX y coordY separados por coma ").split(","))
            #RECURSIVIDAD, El metodo se llama a sí mismo.Asi mientras entre en el 2º elif se repetira la funcion
            return self.comprobar_disparo_jugador(cordX,cordY,tablero)
        return disparo

    def comprobar_disparo_maquina(self,coordX,coordY,tablero):
        if tablero[coordX,coordY] == " ":
            disparo = SIMBOLOS["AGUA"]
            print(f"La máquina ha disparado a ({coordX,coordY} y ha fallado. :))))")
        elif tablero[coordX,coordY] == SIMBOLOS["BARCO"]:
            disparo = SIMBOLOS["IMPACTO"]
            print(f"la maquina ha disparado en las coordenadas {coordX,coordY} y ha tocado barco")
        elif tablero[coordX,coordY] == SIMBOLOS["IMPACTO"] or (tablero[coordX,coordY] == SIMBOLOS["AGUA"]):
            #print("Ya has disparado en esas coordenadas,prueba de nuevo")
            coordX,coordY = np.random.randint(0,10,size=2)
            #RECURSIVIDAD, El metodo se llama a sí mismo.Asi mientras entre en el 2º elif se repetira la funcion
            return self.comprobar_disparo_maquina(coordX,coordY,tablero)
        return disparo
    
        


    def disparo_maquina(self,tablero):
        coor_X,coor_Y = np.random.randint(0,10,size=2)
        disparo = self.comprobar_disparo_maquina(coor_X,coor_Y,tablero)
        time.sleep(3)
        tablero[coor_X,coor_Y] = disparo
        print("Tu tablero\t\t\tTablero de la maquina")
        tab1 = self.mostrar_tablero(tablero)
        tab2 = self.mostrar_tablero(self.tablero,ocultar_barcos=True)
        self.mostrar_tableros_lado_a_lado(tab1,tab2)
        return disparo

    def disparo_jugador(self,tablero):
        coordX,coordY = self.introducir_coordenadas()
        disparo = self.comprobar_disparo_jugador(coordX,coordY,tablero)
        tablero[coordX,coordY] = disparo
        self.disparos_realizados[coordX,coordY] = 1
        time.sleep(3)
        tab1 = self.mostrar_tablero(tablero,ocultar_barcos=True)
        tab2 = self.mostrar_disparos_realizados()
        print("Tablero de la maquina:\t\t\t Tu tablero de disparos:")
        self.mostrar_tableros_lado_a_lado(tab1,tab2)
        return disparo

    def tablero_disparos(self,coordenadas, impacto):
        Fila, columna = coordenadas[0] , coordenadas[1] 
        self.disparos_realizados[Fila, columna] = impacto

    def verificar_victoria(self,tablero):
        if np.any(tablero == SIMBOLOS["BARCO"]):
            return False
        else:
            print("Felicidades, has hundido todos los barcos del rival!")
            return True

    def mostrar_tableros_lado_a_lado(self,tablero1, tablero2):
        for linea1,linea2 in zip(tablero1,tablero2):
            print(f"{linea1}\t\t{linea2}")


            
    
