import pickle

columns = ['A','B','C','D','E','F','G','H']

board_color = {
                    "white": "bt,bh,bb,bq,bk,bb,bh,bt,/,8,bp,/,0,8,wp,/,wt,wh,wb,wq,wk,wb,wh,wt,/",
                    "black": "wt,wh,wb,wq,wk,wb,wh,wt,/,8,wp,/,0,8,bp,/,bt,bh,bb,bq,bk,bb,bh,bt,/"
                }

class Game():
    def __init__(self, color):
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


    def __setattr__(self, name, value):
        self.__dict__[name] = value
        self.__save()


    def update(I, F, check, checkmate):
        self.board[I['r']][I['c']] = 0
        self.board[F['r']][F['c']] = I['p']
        self.check = check
        self.checkmate = checkmate
        with open('bin/moves', 'a+') as moves:
            pickle.dump(f"{self.turn}: {columns[I['c']]}{I['r']} - {columns[F['c']]}{F['r']}\n", moves)

        if self.turn == 'white':
            self.turn = 'black'
            
        else:
            self.turn = 'white'


    def __save(self):
        with open('bin/game', 'wb') as wfile:
            pickle.dump(self, wfile)

def gameRead():
    with open('bin/game', 'rb') as rfile:
        return pickle.load(rfile)
            