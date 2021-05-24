from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

    #   Bloque de Instrucciones
def _BoardResize(event):
    global new_img, cell_size
    widget = event.widget
    board_height = event.height
    cell_size = (event.height - 2 * board_borderwidth) / 8
    resized_img = img.resize((int(cell_size), int(cell_size)), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(resized_img)

def _GetButton(event):
        widget = event.widget
        identity = widget.winfo_id()
        x = widget.winfo_x()
        y = widget.winfo_y()
        print(x, y)

def _CellResize(event):
        widget = event.widget
        widget['width'] = cell_size
        pos = cell_size / 2
        widget.create_image(pos, pos, image = new_img_select, anchor = CENTER)
    #   Fin del Bloque de Instrucciones


window = Tk()
window.title("Furey's Chess")
max_window_width = int(window.winfo_screenwidth() / 2)
max_window_height = int(window.winfo_screenheight() / 2)
max_window_size = f'{max_window_width}x{max_window_height}'
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.geometry(max_window_size)

board_height = max_window_height
board_borderwidth = 10
img = Image.open("piezas/bb.png")
img_select = Image.open("piezas/select.png")

cell_size = (board_height - 2 * board_borderwidth) / 8
resized_img = img.resize((int(cell_size), int(cell_size)), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resized_img)
resized_img_select = img_select.resize((int(cell_size), int(cell_size)), Image.ANTIALIAS)
new_img_select = ImageTk.PhotoImage(resized_img_select)

board = ttk.Frame(window, borderwidth = board_borderwidth, relief = 'sunken')
board.grid(sticky = (N, W, S))

color1 = '#D76849'
color2 = '#632716'
color3 = '#845F54'
color4 = '#77483B'
board_ordercolor = [color1, color2]


for rows in range(8):
    board.rowconfigure(rows, weight = 1, pad = 0)
    for columns in range(8):
        board.columnconfigure(columns, weight = 1, pad = 0)
        pos = rows * 8 + columns
        canva = Canvas(board, borderwidth = 0, width = cell_size, highlightthickness = 0)
        if (columns + rows) % 2 == 0:
            canva.configure(background = board_ordercolor[0])

        else:
            canva.configure(background = board_ordercolor[1])

        pieza = Canvas(canva, borderwidth = 0, width = cell_size, highlightthickness = 0)
        pieza.create_image(0, 0, image = new_img, anchor = NW)

        pieza.grid(row = 0, column = 0, sticky = NSEW)
        canva.grid(row = rows, column = columns, sticky = NSEW)
        canva.bind('<ButtonPress-1>', _GetButton)
        canva.bind('<Configure>', _CellResize)

    board.bind('<Configure>', _BoardResize)

window.mainloop()
