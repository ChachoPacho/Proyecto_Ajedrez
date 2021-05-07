from rules import Class_Ajedrez
import numpy as np
from bases import CrearTablero

def Iniciar_Tablero(mode):
    """
    :param mode: None{} Blancas{B}, Negras{N}
    :return:
    """
    data = Class_Ajedrez(CrearTablero(), "Blanco")
    if mode == None:
        return data
    
    for i in data.piezas:
        data.tablero[i] = data.piezas[i].pieza
    
    data.Turno(True)

    if mode == "B":
        return data
    
    elif mode == "N":
        tablero = list(data.tablero)
        tablero.reverse()
        data.tablero = np.array(tablero)
        return data

def Iniciar_Juego(data):


if __name__ == "__main__":
    ""