class Movements():
    def __init__(self, pos, game):
        self.row, self.col = pos
        self.board = game.board
        self.board_color = game.color[0]
        self.piece = self.board[self.row][self.col]     #   Two letters: [0]:color, [1]:piece


    #   Movements validator
    def __valid_path(self, sr, sc) -> list:     # returns a list of all the posibles ways to move
        moves = []
        row = self.row
        col = self.col
        while True:
            row += sr
            col += sc
            if row > 7 or col > 7 or row < 0 or col < 0: break  # outs the board

            piece = self.board[row][col]    #   Two letters: [0]:color, [1]:piece
            if self.piece[0] == piece[0]: break # same team
            else: moves += [[row, col]] # different team

            if self.piece[0] != piece[0] and piece[0] != '0': break # if different team

        return moves


    #   Main movements
    def horse(self) -> list:
        moves_list = []
        for d in [1, 2]:    # movements in x: 1 or 2
            for r in [-1, 1]:   # movements: top or bott
                row = self.row + (d - 3) * r
                if not (row > 7 or row < 0):    # filter
                    for c in [-1, 1]:   # movements: right or left
                        col = self.col + d * c
                        if not (col > 7 or col < 0):  # filter
                            if self.piece[0] != self.board[row][col][0]:
                                moves_list += [[row, col]]

        return moves_list


    def bishop(self) -> list:
        moves_list = []
        for sr in [1, -1]:
            for sc in [-1, 1]: moves_list += self.__valid_path(sr, sc)

        return moves_list


    def tower(self) -> list:
        moves_list = []
        for sr in [1, -1]: moves_list += self.__valid_path(sr, 0)

        try:
            if self.piece[1] != 'p':
                for sc in [1, -1]: moves_list += self.__valid_path(0, sc)

        except: 
            for sc in [1, -1]: moves_list += self.__valid_path(0, sc)

        return moves_list


    #   Pieces Validators
    def pawn(self):
        moves = []
        for move in self.tower():
            enemy = self.board[move[0]][move[1]]
            if len(moves) == 2 or (len(moves) == 1 and (self.row not in [6,1])): break
            if enemy[0] != self.piece[0] and enemy[0] != '0': continue

            if self.piece[0] == self.board_color:
                if self.row > move[0]: moves += [move]

            elif self.row < move[0]: moves += [move]

        for move in self.bishop():
            enemy = self.board[move[0]][move[1]]
            if self.board[move[0]][move[1]][0] == '0' or (move[1] - self.col) not in [-1, 1]: continue
            if self.piece[0] == self.board_color:
                if self.row > move[0]: moves += [move]

            elif self.row < move[0]: moves += [move]

        return moves


    def king(self):
        moves = []
        for move in self.bishop() + self.tower():
            if self.row == move[0] and (self.col - move[1]) in [-1, 1]: moves += [move]
            elif self.col == move[1] and (self.row - move[0]) in [-1, 1]: moves += [move]
            elif (self.col - move[1]) in [-1, 1] and (self.row - move[0]) in [-1, 1]: moves += [move]

        return moves


    @property
    def moves_list(self) -> list:
        if self.piece == '0': return []

        if self.piece[1] in ['t', 'q']: yield self.tower()

        if self.piece[1] in ['b', 'q']: yield self.bishop()

        if self.piece[1] == 'h': yield self.horse()

        if self.piece[1] == 'p': yield self.pawn()

        if self.piece[1] == 'k': yield self.king()

    
    @property
    def elemental_moves(self):
        yield self.tower()
        yield self.bishop()
        yield self.horse()


    #   Special for CheckMate
    def _stopcheck(self, color):
        self.piece = color + 'p'
        for move in self.tower():
            enemy = self.board[move[0]][move[1]]
            if enemy == '0': continue
            if enemy[1] != 'p': continue

            dif = move[0] - self.row

            if (dif in [2, -2] and move[0] in [6,1]) or dif in [-1, 1]:
                if enemy[0] == self.board_color:
                    if  move[0] > self.row: return move

                elif move[0]  < self.row: return move


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
    