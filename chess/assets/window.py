from os import name, stat
from sys import flags
from tkinter import *    
from tkinter import ttk
from chess.clases.config import Config
from chess.assets.board import Board


#   Creates the window where the interface will be
class Window:
    window = Tk()
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.resizable(0,0)

    def __init__(self, window_name):
        self.font = ('Helvetica', 15)
        self.width = 740 # self.window.winfo_screenwidth()
        self.height = 740 # self.window.winfo_screenheight()

        self.window.title(window_name)
        self.window.geometry(f'{self.width}x{self.height}')

        self.menu()
        self.main_frame()


    def menu(self):
        menu = Menu(self.window, font=self.font, activebackground='#FFFFFF', background='#D0D0D0', foreground='black', border=0)
        menu.add_command(label="Nueva Partida", command=self.__new_game)
        menu.add_command(label="Cargar Partida", command=self.__load_game)
        menu.add_command(label="Guardar", command=self.__save_game)
        #menu.add_command(label="Ayuda", command=self.__help)
        self.window.config(menu = menu)

    
    def main_frame(self):
        #   main_frame creation, where all will be included
        self.main_frame = ttk.Frame(self.window, width=self.width, height=self.height)
        self.main_frame.grid(row=0, column=0, sticky=NSEW)
        self.main_frame.rowconfigure([0], weight=1)
        self.main_frame.columnconfigure([0, 1], weight=1)


    def __new_game(self):
        self.color = ''

        def create():
            if len(text.get(1.0, END)[:10]) < 3 or self.color == '': return
            Config().new_game(text.get(1.0, END)[:-1], 'w')
            trash_win.destroy()
            self.board = Board(self)
            self.board._board(save_file=True)

        def write(_):
            if len(text.get(1.0, END)) > 10:
                chars = text.get(1.0, END)[:10]
                text.delete(1.0, END)
                text.insert(1.0, chars)

        def color(c):
            self.color = c.widget['bg'][0]
            c.widget['bg'][0]

        trash_win = Toplevel(self.window, padx=5, pady=5)
        trash_win.winfo_toplevel().title("Crear Partida")
        trash_win.resizable(0,0)

        title = Label(trash_win, padx=0, pady=5, height=1, font=self.font, text='Nombre de la partida:', justify=LEFT)
        title.grid(column=0, row=0, pady=5)

        text = Text(trash_win, font=self.font, height=1, width=25, spacing1=5, spacing3=5, wrap='none')
        text.bind('<Key>', write)
        text.grid(column=1, row=0, columnspan=2, padx=5)
        text.focus_set()

        title = Label(trash_win, padx=0, pady=5, height=1, font=self.font, text='Color:', justify=LEFT)
        title.grid(column=0, row=1, padx=1)

        white_btn = Button(trash_win, text='Blanco', font=self.font, background='white', foreground='black', activebackground='black', activeforeground='white')
        white_btn.bind('<ButtonPress-1>', color)
        white_btn.grid(column=1, row=1, padx=5)

        black_btn = Button(trash_win, text='Negro', font=self.font, background='black', foreground='white', activebackground='white', activeforeground='black')
        black_btn.bind('<ButtonPress-1>', color)
        black_btn.grid(column=2, row=1, padx=5)

        save_btn = Button(trash_win, text='Crear', font=self.font, command=create)
        save_btn.grid(column=2, row=2, pady=5)


    def __load_game(self):
        color_selected = '#A0A0FF'

        def select(_):
            _iter = listbox.curselection()[0]
            if _iter % 3 == 0:
                Config().load_game(listbox.get(_iter))
                trash_win.destroy()
                self.board = Board(self)
                self.board._board(True)

        def delete(_):
            _item = listbox.curselection()[0]
            if _item % 3 == 0:
                Config().delete_game(listbox.get(_item))
                for i in range(3):
                    listbox.delete(_item)

        trash_win = Toplevel(self.window, padx=5, pady=5)
        trash_win.winfo_toplevel().title("Cargar Partida")
        trash_win.resizable(0,0)

        title = Frame(trash_win, bg='#A0A0A0', highlightthickness=0, border=0, padx=0, pady=0)
        title.grid(column=0, columnspan=2, row=0, sticky=NSEW)

        title1 = Label(title, padx=25, pady=5, height=1, font=self.font, text='Nombre de la partida', bg='#A0A0A0')
        title2 = Label(title, padx=25, pady=5, height=1, font=self.font, text='Fecha', bg='#A0A0A0')
        title1.grid(column=0, row=0, sticky=(NW, S))
        title2.grid(column=1, row=0, sticky=(NW, S))

        trash_frame = Canvas(trash_win, highlightthickness=0, border=0)
        trash_frame.grid(column=0, columnspan=2, row=1, sticky=NSEW, padx=25, pady=0)

        scrollbar = Scrollbar(trash_frame, orient=VERTICAL)
        listbox = Listbox(trash_frame, font=self.font, bg='white', yscrollcommand=scrollbar.set, highlightthickness=5, selectbackground=color_selected, selectmode=SINGLE, width=0, height=8, relief=SOLID, border=0, highlightcolor='white')
        
        row = 0
        for save in Config().list_games:
            listbox.insert(END, save[0], ' ' * len(save[1]) + save[1], '-' * len(save[1]) * 2)
            listbox.itemconfigure(row + 1, foreground='gray', selectforeground='gray', selectbackground='white')
            listbox.itemconfigure(row + 2, selectbackground='white', background='white')
            row += 3

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y, pady=(20, 100))
        listbox.pack(fill=BOTH, padx=25, pady=(25, 0))

        save_btn = Button(trash_frame, text='Seleccionar', font=self.font)
        del_btn = Button(trash_frame, text='Eliminar', font=self.font)

        save_btn.bind('<ButtonPress-1>', select)
        del_btn.bind('<ButtonPress-1>', delete)
        listbox.bind('<Double-ButtonPress-1>', select)

        save_btn.pack(side=RIGHT, padx=25, pady=25)
        del_btn.pack(side=LEFT, padx=25, pady=25)
        listbox.focus_force()


    def __save_game(self):
        if Config().issaved: return

        def save():
            if len(text.get(1.0, END)) > 3:
                Config().save_game(text.get(1.0, END)[:10])
                trash_win.destroy()

        def write(_):
            if len(text.get(1.0, END)) > 10:
                chars = text.get(1.0, END)[:10]
                text.delete(1.0, END)
                text.insert(1.0, chars)

        trash_win = Toplevel(self.window, padx=5, pady=5)
        trash_win.winfo_toplevel().title("Guardar Partida")
        trash_win.resizable(0,0)

        title = Label(trash_win, padx=0, pady=5, height=1, font=self.font, text='Inserta el Nombre de la partida:', justify=LEFT)
        title.grid(column=0, row=0)

        text = Text(trash_win, font=self.font, height=1, width=25, spacing1=5, spacing3=5, wrap='none')
        text.bind('<Key>', write)
        text.grid(column=0, row=1)
        text.focus_set()

        save_btn = Button(trash_win, text='Guardar', font=self.font, command=save)
        save_btn.grid(column=1, row=1)


    def __help(self):
        ""


    def start(self):
        self.board = Board(self)
        self.board._board(Config().issaved)
        self.window.mainloop()

