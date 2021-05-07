from iniz import IniciarTablero

def Iniciar_Juego():
    tablero = IniciarTablero(None)
    tablero.MostrarTablero()
    menu0 = 1
    while not menu0 == 0:
        # try:
        menu = int(input("""¿Desea iniciar una nueva partida?
                       Sí: 1
                       No: 0
                       Respuesta: """))

        if menu0 == 1:
            while not menu == 0:
                # try:
                menu = int(input("""¿Qué quieres jugar?
                        Blancas: 1
                        Negras: 2
                        Salir: 0
                        Respuesta: """))
                if menu == 2 or menu == 1:
                    if menu == 1:
                        tablero = IniciarTablero("B")

                    else:
                        tablero = IniciarTablero("N")

                    tablero.MostrarTablero()
                    modif = True
                    while modif == True:
                        # try:
                        tablero.ModificarTablero()
                        if tablero.ModificarTablero() == True:
                            modif == True


# """
#                                 except:
#                                     print("\tAlgo salió mal en las Modificaciones\n")

#                         else:
#                             print("\tVuelve a intentarlo\n")

#                     except:
#                         print("\tAlgo en la Elección de Juego salió mal\n")

#             else:
#                 print("\tVuelve a intentarlo\n")

#         except:
#             print("\tAlgo en el Inicio de Partida salió mal\n")
# """

if __name__ == "__main__":
    Iniciar_Juego()
