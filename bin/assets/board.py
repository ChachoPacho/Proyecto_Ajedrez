from Ajedrez.bin.tools import img_resizer, ListIMG_PR, ListIMG_SR, data_storage
from Ajedrez.bin.view import Window
from tkinter import ttk
from tkinter import *


class Board:
    board_border_width = 10
    standard_color = []
    shadow_color = []

    def __init__(self):
        #   Creation
        game_zone = ttk.Frame(Window.main_frame)
        game_zone.grid(row=1, sticky=NSEW)
        game_zone.rowconfigure(0, weight=1)
        game_zone.columnconfigure([0, 1], weight=0)
        # game_zone.bind('<Configure>', self._full_board_frame_resize)

        decorated_board = ttk.Frame(game_zone, borderwidth=self.board_border_width, relief='sunken')
        decorated_board.grid(row=0, column=0, sticky=NW)

        board_size = 720
        self.cell_size = int(board_size / 8) - 1 / 8

        decorated_board['width'] = decorated_board['height'] = board_size

        self.board_chat = Text(game_zone, borderwidth=0, state='disabled', font=('Helvetica', 15))
        self.board_chat.grid(row=0, column=1, sticky=NE)

        self.board = Canvas(decorated_board, highlightthickness=0, bd=0)
        self.board.grid(row=0, column=0, sticky=NSEW)
        self.board.bind('<ButtonPress-1>', self._get_button)
        # canvas.bind('<Configure>', self._cell_resize)

        self.board['width'] = self.board['height'] = board_size
        self.board_chat['height'] = board_size
        self.board_chat['height'] = Window.main_frame['width'] - board_size

        img_resizer(90)

    def start_color(self, starts='white'):
        _color = data_storage('board', 'color', 'standard')
        _shadow_color = data_storage('board', 'color', 'shadow')
        if starts == 'white':
            self.standard_color = _color
            self.shadow_color = _shadow_color

        elif starts == 'black':
            self.standard_color = _color.reverse
            self.shadow_color = _shadow_color.reverse

    def __board_chat_writer(self, msg):
        self.board_chat['state'] = 'normal'
        self.board_chat.insert('end', msg)
        self.board_chat['state'] = 'disabled'

    def _board(self):
        for rows in range(8):
            for columns in range(8):
                top = rows * self.cell_size
                bottom = top + self.cell_size
                left = columns * self.cell_size
                right = left + self.cell_size
                if (columns + rows) % 2 == 0:
                    self.board.create_rectangle(left, top, right, bottom, fill=self.standard_color[0], tag='board')
                    self.board.create_image(right - self.cell_size / 2, bottom - self.cell_size / 2, image=ListIMG_PR['wb'], anchor=CENTER, tag='bb')

                else:
                    self.board.create_rectangle(left, top, right, bottom, fill=self.standard_color[1], tag='board')
                    self.board.create_image(right - self.cell_size / 2, bottom - self.cell_size / 2, image=ListIMG_PR['wb'], anchor=CENTER, tag='bb')

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

    def _get_button(self, event):
        x = event.x / self.cell_size
        y = event.y / self.cell_size

        self.__board_chat_writer(f'{int(x) + 1} {int(y) + 1}\n')
        xd = self.board.create_image(45, 45, image=ListIMG_PR['wb'], anchor=CENTER, tag='bb')
        print(event.widget.find('withtag', 'bb'))
        event.widget.itemconfigure('bb', image=ListIMG_PR['bb'])

    def _cell_resize(self, event):
        widget = event.widget
        widget['width'] = widget['height'] = self.cell_size
        pos = int(self.cell_size / 2)
        widget.create_image(pos, pos, image=ListIMGResized['bb'], anchor=CENTER)

    #   Instruction block end

