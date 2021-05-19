from Clases.check import Check
from Clases.moves import Movements


def Checkmate(test, checks, turn):
    if turn == 'b': color = 'w'
    else: color = 'b'
    king = test.kings[color]

    for check in checks[color]:
        if check != []:
            checkmate = Check(test, [check])[turn]
            if checkmate == []:
                movements = Movements(check, test).elemental_moves
                for moves in movements:
                    if king in moves:
                        moves.remove(king)
                        if list(Check(test, moves, mode = 'full').values())[0] == [[]]:
                            for move in moves:
                                if Movements(move, test)._stopcheck(turn): return False

                            for move in Movements(king, test).king():
                                I = { 'r': king[0], 'c': king[1] }
                                F = { 'r': move[0], 'c': move[1] }
                                test.update(I, F)
                                if Check(test, [move])[color] == [[]]: return False
                                test.update(F, I)

                return color

    return False
