import pickle
import os
import shutil


class Board():
    def __init__(self, mode = 'game'):
        try:
            with open(cwd + '/bin/' + mode + 'board', 'rb') as rfile: data = pickle.load(rfile)

        except: 
            shutil.copyfile(cwd + '/bin/gameboard', cwd + '/bin/' + mode + 'board')
            with open(cwd + '/bin/' + mode, 'rb') as rfile: data = pickle.load(rfile)

        finally: 
            for name in data.__dict__: self.__setattr__(name, data.__dict__[name])
            self.__setattr__('mode', mode)


    def __setattr__(self, name, value):
        self.__dict__[name] = value
        with open(cwd + '/bin/' + self.mode + 'board', 'wb') as wfile: pickle.dump(self, wfile)

    
    def end(self):
        os.remove(cwd + '/bin/' + self.mode + 'board')


    def start(self, color):
        str_board = board_color[color].split(',')
        board = []
        line = []
        for n in range(len(str_board)):
            if str_board[n] == 'wp' or str_board[n] == 'bp': continue

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
        if color == 'black': c.reverse()
        self.kings = {c[0]: [0, 4], c[1]: [7, 4]}


    def update(self, I, F):
        p = self.board[I['r']][I['c']]
        if p in ['bk', 'wk']: self.kings[p[0]] = [F['r'], F['c']]

        self.board[F['r']][F['c']] = self.board[I['r']][I['c']]
        self.board[I['r']][I['c']] = '0'
