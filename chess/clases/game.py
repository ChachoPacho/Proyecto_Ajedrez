from chess.clases.board import Board
from chess.clases.movements import Check, Checkmate
from chess.constants import BIN
import pickle


class Game():
    def __init__(self):
        try:
            with open(BIN + 'game', 'rb') as rfile: data = pickle.load(rfile)
            for name in data.__dict__: self.__setattr__(name, data.__dict__[name])

        except: ''
            

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        with open(BIN + 'game', 'wb') as wfile: pickle.dump(self, wfile)


    def start(self, color):
        self.board_data = Board()
        self.board_data.start(color)

        self.turn = 'w'
        self.check = {'b': [], 'w': []}
        self.checkmate = False


    def update(self, I, F):
        test = Board(mode = 'test')
        test.update(I, F)
        check = Check(test, test.kings.values())
        checkmate = Checkmate(test, check, self.turn)
        del test
        if check[self.turn] == []:
            self.board_data.update(I, F)
            self.check = check
            self.checkmate = checkmate
            if self.turn == 'w': self.turn = 'b'
                
            else: self.turn = 'w'
            
            return True

        return False
