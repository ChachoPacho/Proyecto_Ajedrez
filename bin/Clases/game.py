from Clases.board import Board
import pickle
import os
import shutil

cwd = os.path.dirname(__file__)

columns = ['A','B','C','D','E','F','G','H']
board_color = {
                    "white": "bt,bh,bb,bq,bk,bb,bh,bt,/,8,bp,/,0,8,wp,/,wt,wh,wb,wq,wk,wb,wh,wt,/",
                    "black": "wt,wh,wb,wq,wk,wb,wh,wt,/,8,wp,/,0,8,bp,/,bt,bh,bb,bq,bk,bb,bh,bt,/"
                }

class Game():
    def __init__(self, mode = 'game'):
        try:
            with open(cwd + '/bin/' + mode, 'rb') as rfile: data = pickle.load(rfile)

        except: 
            shutil.copyfile(cwd + '/bin/game', cwd + '/bin/' + mode)
            with open(cwd + '/bin/' + mode, 'rb') as rfile: data = pickle.load(rfile)

        finally: 
            for name in data.__dict__: self.__setattr__(name, data.__dict__[name])
            self.__setattr__('mode', mode)


    def __setattr__(self, name, value):
        self.__dict__[name] = value
        with open(cwd + '/bin/' + self.mode, 'wb') as wfile: pickle.dump(self, wfile)

    
    def end(self):
        os.remove(cwd + '/bin/' + self.mode)


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
        self.turn = 'white'
        self.checkmate = False
        c = ['b', 'w']
        if color == 'black': c.reverse()
        self.kings = {c[0]: [0, 4], c[1]: [7, 4]}


    def update(self, I, F, checkmate):
        p = self.board[I['r']][I['c']]
        if p in ['bk', 'wk']: self.kings[p[0]] = [F['r'], F['c']]

        self.board[F['r']][F['c']] = self.board[I['r']][I['c']]
        self.board[I['r']][I['c']] = '0'

        self.checkmate = checkmate
        if self.turn == 'white': self.turn = 'black'
            
        else: self.turn = 'white'
