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
                