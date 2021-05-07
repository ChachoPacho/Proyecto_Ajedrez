from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#   Creates the window where the interface will be
class Window:
    window = Tk()
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    def __init__(self, window_name):
        self.window.title(window_name)
        self._prepare_window()

    def _prepare_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        self.window.geometry(f'{screen_width}x{screen_height}')

        #   main_frame creation, where all will be included
        self.main_frame = ttk.Frame(self.window, width=screen_width, height=screen_height)
        self.main_frame.grid(row=0, column=0, sticky=NSEW)
        self.main_frame.rowconfigure([0], weight=1)
        self.main_frame.columnconfigure([0, 1], weight=1)

    def open_window(self):
        self.window.mainloop()

