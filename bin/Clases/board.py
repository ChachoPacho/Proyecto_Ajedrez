import pickle
import os
import shutil


columns = ['A','B','C','D','E','F','G','H']
board_color = {
                    "w": "bt,bh,bb,bq,bk,bb,bh,bt,/,8,bp,/,0,8,wp,/,wt,wh,wb,wq,wk,wb,wh,wt,/",
                    "b": "wt,wh,wb,wq,wk,wb,wh,wt,/,8,wp,/,0,8,bp,/,bt,bh,bb,bq,bk,bb,bh,bt,/"
                }
cwd = os.path.dirname(__file__) + '/bin/'


class Board():
    def __init__(self, mode = 'game'):
        try:
            with open(cwd + 'gameboard', 'rb') as rfile: data = pickle.load(rfile)
            for name in data.__dict__: self.__setattr__(name, data.__dict__[name])

        except: ''

        finally: self.__setattr__('mode', mode)   


    def __setattr__(self, name, value):
        self.__dict__[name] = value


    def __save(self):
        if self.mode == 'game':
            with open(cwd + self.mode + 'board', 'wb') as wfile: pickle.dump(self, wfile)


    def start(self, color):
        str_board = board_color[color].split(',')
        board = []
        line = []
        for n in range(len(str_board)):
            if str_board[n] in ['wp', 'bp']: continue

            elif str_board[n] == '/':
                board += [line]
                line = []

            elif str_board[n] == '8': line += [str_board[n+1]] * 8

            elif str_board[n] == '0':
                for row in range(4): board += [['0'] * 8]

            else: line += [str_board[n]]

        self.board = board
        self.color = color
        c = ['b', 'w']
        if color == 'b': c.reverse()
        self.kings = {c[0]: [0, 4], c[1]: [7, 4]}
        self.__save()


    def update(self, I, F):
        p = self.board[I['r']][I['c']]
        if p in ['bk', 'wk']: self.kings[p[0]] = [F['r'], F['c']]

        self.board[F['r']][F['c']] = self.board[I['r']][I['c']]
        self.board[I['r']][I['c']] = '0'
        self.__save()
