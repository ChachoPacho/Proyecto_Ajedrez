import pickle
import os

cwd = os.path.dirname(__file__)

columns = ['A','B','C','D','E','F','G','H']
board_color = {
                    "white": "bt,bh,bb,bq,bk,bb,bh,bt,/,8,bp,/,0,8,wp,/,wt,wh,wb,wq,wk,wb,wh,wt,/",
                    "black": "wt,wh,wb,wq,wk,wb,wh,wt,/,8,wp,/,0,8,bp,/,bt,bh,bb,bq,bk,bb,bh,bt,/"
                }

class Game():
    def __init__(self):
        try:
            with open(cwd + '/bin/game', 'rb') as rfile:
                data = pickle.load(rfile)

            for name in data.__dict__:
                self.__setattr__(name, data.__dict__[name])

        except:
            ""


    def __setattr__(self, name, value):
        self.__dict__[name] = value
        self.__save()


    def start(self, color):
        str_board = board_color[color].split(',')
        board = []
        line = []
        for n in range(len(str_board)):
            if str_board[n] == 'wp' or str_board[n] == 'bp':
                continue

            elif str_board[n] == '/':
                board += [line]
                line = []

            elif str_board[n] == '8':
                line += [str_board[n+1]] * 8

            elif str_board[n] == '0':
                for row in range(4):
                    board += [['0'] * 8]

            else:
                line += [str_board[n]]

        self.board = board
        self.color = color
        self.turn = 'white'
        self.check = None
        self.checkmate = False


    def update(self, I, F, check, checkmate):
        print(self.board[F['r']][F['c']])
        self.board[F['r']][F['c']] = self.board[I['r']][I['c']]
        print(self.board[F['r']][F['c']])
        self.board[I['r']][I['c']] = '0'
        self.check = check
        self.checkmate = checkmate
        if self.turn == 'white':
            self.turn = 'black'
            
        else:
            self.turn = 'white'


    def __save(self):
        with open(cwd + '/bin/game', 'wb') as wfile:
            pickle.dump(self, wfile)
