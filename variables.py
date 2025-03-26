import numpy as np

# Dimensiones del tablero
TABLERO_SIZE = 10

# Diccionario de Barcos (nombre: eslora, cantidad)
BARCOS = {
    "Destructor": (1, 4),
    "Submarino": (2, 3),
    "Crucero": (3, 2),
    "Acorazado": (4,1)
}

# Caracteres para representar el tablero
AGUA = "-"    # Agua sin disparos
BARCO = "B"   # Barco colocado
IMPACTO = "X" # Disparo que acierta en un barco
FALLO = "O"   # Disparo fallido

#Aqui se podria hacer algo tipo 
SIMBOLOS = { "AGUA": "-",
              "BARCO":"B",
              "IMPACTO":"X",
              "FALLO":"O" }