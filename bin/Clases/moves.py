from Clases.game import Game

class Movements():
    def __init__(self, pos):
        self.game = Game()
        self.row, self.col = pos
        self.board = self.game.board
        self.board_color = self.game.color[0]
        self.piece = self.board[self.row][self.col]     #   Two letters: [0]:color, [1]:piece

    def __valid_pawn(self):
        b = self.__bishop()
        t = self.__tower()
        moves = []
        for move in t:
            if len(moves) == 2 or (len(moves) == 1 and (self.row not in [6,1])):
                break

            if self.piece[0] == self.board_color:
                if self.row > move[0]:
                    moves += [move]

            elif self.row < move[0]:
                moves += [move]

        if len(b) <= 2 and (b[0][0] == b[1][0]):    #   Two movements in the same row, different columns
            moves += b

        return moves

    def __valid_path(self, sr, sc) -> list:     # returns a list of all the posibles ways to move
        moves = []
        row = self.row
        col = self.col
        while True:
            row += sr
            col += sc
            if row > 7 or col > 7 or row < 0 or col < 0:    # outs the board
                break

            piece = self.board[row][col]    #   Two letters: [0]:color, [1]:piece
            if self.piece[0] == piece[0]:   # same team
                break

            else:   # different team
                moves += [[row, col]]

            if self.piece[0] != piece[0] and piece[0] != '0':     # if different team
                break

        return moves

    def __horse(self) -> list:
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

    def __bishop(self) -> list:
        moves_list = []
        for sr in [1, -1]:
            for sc in [-1, 1]:
                moves_list += self.__valid_path(sr, sc)

        return moves_list

    def __tower(self) -> list:
        moves_list = []
        for sr in [1, -1]:
            moves_list += self.__valid_path(sr, 0)

        if self.piece[1] != 'p':
            for sc in [1, -1]:
                moves_list += self.__valid_path(0, sc)

        return moves_list

    @property
    def moves_list(self) -> list:
        if self.piece == '0':
            return []

        if self.piece[1] in ['t', 'q', 'k']:
            yield self.__tower()

        if self.piece[1] in ['b', 'q', 'k']:
            yield self.__bishop()

        if self.piece[1] == 'h':
            yield self.__horse()

        if self.piece[1] == 'p':
            yield self.__valid_pawn()

    @property
    def check(self) -> list:
        def __enemy_in_line(position):
            piece = self.board[position[0]][position[1]]
            if not (piece == '0' or piece[0] == self.piece[0]):
                return piece[1]

            else:
                return '0'

        for move in self.__horse():
            if __enemy_in_line(move) == 'h':
                yield move

        for move in self.__bishop():
            enemy = __enemy_in_line(move)
            if enemy in ['b', 'q', 'p']:
                if enemy == 'p' and abs(move[0] - self.row) > 1:
                    continue

                yield move

        for move in self.__tower():
            if __enemy_in_line(move) in ['t', 'q']:
                yield move
