from Clases.moves import Movements


def Check(test, pieces, mode = 'normal'):
    checks = {}
    boolean = True

    def __enemy_in_line(position):
        piece = moves.board[position[0]][position[1]]
        if piece != '0' and piece[0] != moves.piece[0]: return piece[1]

    for piece in pieces:
        moves_list = []
        moves = Movements([piece[0], piece[1]], test)
        moves.piece = moves.board[piece[0]][piece[1]]

        for move in moves.horse():
            if __enemy_in_line(move) == 'h': moves_list += [move]

        for move in moves.bishop():
            if __enemy_in_line(move) in ['b', 'q']: moves_list += [move]

        for move in moves.tower():
            if __enemy_in_line(move) in ['t', 'q']: moves_list += [move]

        if mode == 'normal':
            for move in moves.king():
                if __enemy_in_line(move) == 'k': moves_list += [move]

        for move in moves.pawn():
            if mode == 'normal': boolean = move[1] != moves.col
            if boolean and __enemy_in_line(move) == 'p': moves_list += [move]

        checks.update({moves.piece[0]: moves_list})

    return checks
        