from tkinter import ttk
from tkinter import *
from chess.clases.game import Game
from chess.clases.movements import Movements
from chess.tools.images import Data, Images, Images_Data
game = Game()
game.start('w')

images_data = Images_Data()


class Board:
    board_border_width = 10

    def __init__(self, Window):
        #   Game Zone:  Decorated Board + Chat
        game_zone = ttk.Frame(Window.main_frame)
        game_zone.grid(row=1, sticky=NSEW)
        game_zone.rowconfigure([0, 1], weight=0)
        game_zone.columnconfigure([0, 1], weight=0)
        # game_zone.bind('<Configure>', self._full_board_frame_resize)

        #   Elements
        board_size = 720
        self.cell_size = int(board_size / 8) - 1 / 8
        self.pieces = Images('pieces', width=self.cell_size, height=self.cell_size).get
        self.specials = Images('specials', width=self.cell_size, height=self.cell_size).get
        self.cell_move = []
        self.cell_attack = []
        self.current_piece = None

        #   Board chat: what happens in the board will be here
        self.board_chat = Text(game_zone, borderwidth=0, state='disabled', font=Window.font)
        self.board_chat['width'] = Window.main_frame['width'] - board_size
        self.board_chat['height'] = board_size
        self.board_chat.grid(row=1, column=1, sticky=NE)

        #   Decorated Board: board + border
        decorated_board = ttk.Frame(game_zone, borderwidth=self.board_border_width, relief='sunken')
        decorated_board['width'] = decorated_board['height'] = board_size
        decorated_board.grid(row=1, column=0, sticky=NW)

        #   Board:  the chessboard basically
        self.board = Canvas(decorated_board, highlightthickness=0, bd=0)
        self.board['width'] = self.board['height'] = board_size
        self.board.grid(row=0, column=0, sticky=NSEW)
        self.board.bind('<ButtonPress-1>', self._get_button)
        # canvas.bind('<Configure>', self._cell_resize)

        self._set_color('standard2')
        

    def _set_color(self, style):
        self.board_color = Data().board['color'][style]
        if game.board_data.color == 'b':
            self.board_color.reverse()


    def __board_chat_writer(self, msg):
        self.board_chat['state'] = 'normal'
        self.board_chat.insert('end', msg)
        self.board_chat['state'] = 'disabled'


    def __select_piece(self, x, y):
        self.board.delete('cell_move')
        if [y, x] not in self.cell_move and game.board_data.board[y][x][0] != game.turn[0]:
            return

        cell = self.cell_size / 2
        widget = f"Y{y}X{x}"
        movements = Movements([y, x], game.board_data)

        if [y, x] not in self.cell_move:
            self.current_piece = widget
            for list_pieces in list(movements.moves_list):
                for piece in list_pieces:
                    top, right, bottom, left = self._positions(piece[0], piece[1])

                    try:
                        images_data.select(f"Y{piece[0]}X{piece[1]}")
                        self.board.create_image(right - cell, bottom - cell, image=self.specials['attack'], anchor=CENTER, tag='cell_move')
                        self.cell_attack.append(piece)

                    except ValueError:
                        self.board.create_image(right - cell, bottom - cell, image=self.specials['select'], anchor=CENTER, tag='cell_move')

                    finally:
                        self.cell_move.append(piece)

            self.board.lift('piece')

        else:
            r = int(self.current_piece[1])
            c = int(self.current_piece[3])
            I = { 'r': r, 'c': c }
            F = { 'r': y, 'c': x }
            if game.update(I, F):
                if [y, x] in self.cell_attack:
                    self.board.delete(images_data.select(widget))
                    images_data.delete(widget)
                    
                self.board.moveto(images_data.select(self.current_piece), (self.cell_size) * x, (self.cell_size) * y)
                images_data.update(f"Y{r}X{c}", widget)
                
            self.cell_move.clear()
            self.cell_attack.clear()


    def _board(self):
        images_data.reset()
        for rows in range(8):
            for columns in range(8):
                #   Positions
                top, right, bottom, left = self._positions(rows, columns)
                
                #   Colors
                if (columns + rows) % 2 == 0:
                    color = self.board_color[0]

                else:
                    color = self.board_color[1]

                #   Elements
                cell = self.cell_size / 2

                self.board.create_rectangle(left, top, right, bottom, fill=color, tag='board')
                if game.board_data.board[rows][columns] != '0': 
                    pos = f'Y{rows}X{columns}'
                    self.board.create_image(right - cell, bottom - cell, image=self.pieces[game.board_data.board[rows][columns]], anchor=CENTER, tag=[pos, 'piece'])
                    images_data.append(pos)
        
        self.board.lift('piece')

    
    def _positions(self, row, column):
        top = row * self.cell_size
        bottom = top + self.cell_size
        left = column * self.cell_size
        right = left + self.cell_size
        return [top, right, bottom, left]


    """
        #   Instruction block
        def _full_board_frame_resize(self, event):
            if event.height > event.width:
                size = event.width

            else:
                size = event.height

            self.board['width'] = self.board['height'] = size
            self.board_chat['height'] = size
            self.board_chat['height'] = event.width - size
            self.cell_size = (size - 2 * self.board_border_width) / 8
            img_resizer(self.cell_size)
    """

    #   All the buttons functions
    def _get_button(self, event):
        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)

        self.__board_chat_writer(str(x + 1) + ' ' + str(y + 1) + '\n')

        self.__select_piece(x, y)


    # def _cell_resize(self, event):
    #     widget = event.widget
    #     widget['width'] = widget['height'] = self.cell_size
    #     pos = int(self.cell_size / 2)
    #     widget.create_image(pos, pos, image=ListIMGResized['bb'], anchor=CENTER)

    #   Instruction block end
