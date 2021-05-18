from Clases.game import Game
import pickle
import os

cwd = os.path.dirname(__file__)


class Movements():
    def __init__(self, pos, mode = 'game'):
        self.game = Game(mode = mode)
        self.row, self.col = pos
        self.board = self.game.board
        self.board_color = self.game.color[0]
        self.piece = self.board[self.row][self.col]     #   Two letters: [0]:color, [1]:piece


    #   Pieces Validators
    def _valid_pawn(self):
        b = self._bishop()
        t = self._tower()
        moves = []
        for move in t:
            enemy = self.board[move[0]][move[1]]
            if len(moves) == 2 or (len(moves) == 1 and (self.row not in [6,1])): break
            if enemy[0] != self.piece[0] and enemy[0] != '0': continue

            if self.piece[0] == self.board_color:
                if self.row > move[0]: moves += [move]

            elif self.row < move[0]: moves += [move]

        for move in b:
            enemy = self.board[move[0]][move[1]]
            if self.board[move[0]][move[1]][0] == '0' or (move[1] - self.col) not in [-1, 1]: continue
            if self.piece[0] == self.board_color:
                if self.row > move[0]: moves += [move]

            elif self.row < move[0]: moves += [move]

        return moves


    def __valid_king(self):
        bt = self._bishop() + self._tower()
        moves = []
        for move in bt:
            if self.row == move[0] and (self.col - move[1]) in [-1, 1]: moves += [move]
            elif self.col == move[1] and (self.row - move[0]) in [-1, 1]: moves += [move]
            elif (self.col - move[1]) in [-1, 1] and (self.row - move[0]) in [-1, 1]: moves += [move]

        return moves


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
    def _horse(self) -> list:
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


    def _bishop(self) -> list:
        moves_list = []
        for sr in [1, -1]:
            for sc in [-1, 1]: moves_list += self.__valid_path(sr, sc)

        return moves_list


    def _tower(self) -> list:
        moves_list = []
        for sr in [1, -1]: moves_list += self.__valid_path(sr, 0)

        if self.piece[1] != 'p':
            for sc in [1, -1]: moves_list += self.__valid_path(0, sc)

        return moves_list


    @property
    def moves_list(self) -> list:
        if self.piece == '0': return []

        if self.piece[1] in ['t', 'q']: yield self._tower()

        if self.piece[1] in ['b', 'q']: yield self._bishop()

        if self.piece[1] == 'h': yield self._horse()

        if self.piece[1] == 'p': yield self._valid_pawn()

        if self.piece[1] == 'k': yield self.__valid_king()


class Check(Movements):
    def __init__(self):
        try:
            with open(cwd + '/bin/check', 'rb') as rfile: data = pickle.load(rfile)

            for name in data.__dict__: self.__setattr__(name, data.__dict__[name])

        except: ""


    def __setattr__(self, name, value):
        self.__dict__[name] = value
        with open(cwd + '/bin/check', 'wb') as wfile: pickle.dump(self, wfile)     


    def restart(self):
        self.checks = {} 


    def state(self) -> list:
        test = Game(mode = 'test')
        def __enemy_in_line(position):
            piece = moves.game.board[position[0]][position[1]]
            if piece != '0' and piece[0] != moves.piece[0]: return piece[1]

        for king in test.kings.values():
            moves_list = []
            moves = Movements([king[0], king[1]], mode = 'test')
            moves.piece = moves.game.board[king[0]][king[1]]

            for move in moves._horse():
                if __enemy_in_line(move) == 'h': moves_list += move

            for move in moves._bishop():
                if __enemy_in_line(move) in ['b', 'q']: moves_list += move

            for move in moves._tower():
                if __enemy_in_line(move) in ['t', 'q']: moves_list += move

            for move in moves._valid_pawn():
                if move[1] != moves.col and __enemy_in_line(move) == 'p': moves_list += move

            self.checks.update({moves.piece[0]: moves_list})

        test.end()
        return self.checks
        