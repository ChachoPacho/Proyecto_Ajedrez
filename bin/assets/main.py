from tkinter import *
from tkinter import ttk


#   Creates the window where the interface will be
class Window:
    window = Tk()
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    def __init__(self, window_name):
        self.window.title(window_name)
        self.font = ('Helvetica', 15)
        self._menu()
        self._prepare_window()
        self._prepare_frame()

    def donothing(self):
        filewin = Toplevel(self.window)
        button = Button(filewin, text="Do nothing button")
        button.pack()


    def _menu(self):
        menu = Menu(self.window, font= self.font)
        menu.add_command(label="New", command=self.donothing)
        menu.add_command(label="Open", command=self.donothing)
        menu.add_command(label="Save", command=self.donothing)
        menu.add_command(label="Save as...", command=self.donothing)
        menu.add_command(label="Close", command=self.donothing)
        self.window.config(menu = menu)


    def _prepare_window(self):
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}')

    
    def _prepare_frame(self):
        #   main_frame creation, where all will be included
        main_frame = ttk.Frame(self.window, width=self.width, height=self.height)
        main_frame.grid(row=0, column=0, sticky=NSEW)
        main_frame.rowconfigure([0], weight=1)
        main_frame.columnconfigure([0, 1], weight=1)
        self.main_frame = main_frame


    def start(self):
        self.window.mainloop()
