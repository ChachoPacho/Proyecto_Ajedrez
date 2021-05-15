from tkinter import *
from tkinter import ttk


#   Creates the window where the interface will be
class Window:
    window = Tk()
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    def __init__(self, window_name):
        self.window.title(window_name)
        self._prepare_window()
        self._prepare_frame()


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
