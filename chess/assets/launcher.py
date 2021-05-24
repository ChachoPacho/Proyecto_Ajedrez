from tkinter import *
import tkinter
from PIL import Image, ImageTk
from chess.tools.images import Images
from chess.constants import BIN, LICENSE, README

#   Creates the window where the interface will be
class Launcher:
    launcher = Tk()
    launcher.columnconfigure(0, weight=1)
    launcher.rowconfigure(0, weight=1)
    launcher.title('PyChessBoard')
    textos = []
    textos += ["PyChessBoard"]
    textos += ["Gracias por jugar"]
    buttons = ['start', 'license', 'readme', 'quit']
    menuButtons = ['start', 'license', 'readme']


    def __init__(self):
        self.width = 720
        self.height = 480
        self.text_font = ['bitstream', '10']
        self.subtitle_font = ['bitstream', '16', 'bold', 'italic']
        self.title_font = ['Helvetica', '40', 'bold']

        self.current_width = 720
        self.current_height = 480

        self.launcher.geometry(f'{self.width}x{self.height}')
        self.main_frame()
        self.launcher.mainloop()


    def menu_buttons(self):
        def btn_create(name, text):
            self.__dict__[name] = Button(self.mainFrame, font=self.subtitle_font, cursor='hand2', width=10, height=2, highlightthickness=0, anchor=CENTER)
            btn = self.__dict__[name]
            btn['text'] = text
            if name != 'start': btn.bind('<ButtonPress>', self._open)
            else: btn.bind('<ButtonPress>', self.__open_board)

        btn_create('start', 'Empezar')
        btn_create('license', 'LICENCIA')
        btn_create('readme', 'Read Me')


    def main_frame(self):
        #   main_frame creation, where all will be included
        self.mainFrame = Canvas(self.launcher, bd=0, highlightthickness=0)
        self.mainFrame.bind('<Configure>', self._resize_mf)
        self.mainFrame.grid(column=0, row=0, sticky=NSEW)

        self.mainFrame.create_image(0, 0, tag='image', anchor=NW)
        self.mainFrame.create_text(0, 0, tags='texto')

        self.menu_buttons()


    def _cleanMF(self):
        for btn in self.buttons:
            if btn in self.__dict__:
                self.__dict__[btn].destroy()
                del(self.__dict__[btn])

        self.mainFrame.delete('texto')


    def _resize_mf(self, event):
        w = event.width
        h = event.height

        self.image = Images('backgrounds', width=w, height=h).get['chessboard']
        self.mainFrame.itemconfig('image', image=self.image)

        if self.mainFrame.find_withtag('texto') != (): self._text(w, h)
        if 'start' in self.__dict__: self._buttons(w, h)
        else:
            for btn in self.menuButtons:
                if btn in self.__dict__:
                    self._open(btn, w, h)

        self.current_width = w
        self.current_height = h


    def _text(self, width, height):
        self.mainFrame.delete('texto')

        title_font = self.title_font.copy()
        font = self.subtitle_font.copy()
        dif = width / self.width

        title_font[1] = f'{int(float(self.title_font[1]) * dif)}'
        w = int(width * 0.5)
        h = int(height * 0.1)
        f = int(float(title_font[1]) * 0.075)
        self.mainFrame.create_text(w, h, tags='texto', text=self.textos[0], font=title_font, anchor=CENTER)
        self.mainFrame.create_text(w + f, h - f, tags='texto', text=self.textos[0], font=title_font, anchor=CENTER, fill='white')

        font[1] = f'{int(float(self.subtitle_font[1]) * dif)}'
        w = int(width * 0.8)
        h = int(height * 0.95)
        f = int(float(font[1]) * 0.1)
        self.mainFrame.create_text(w, h, tags='texto', text=self.textos[1], font=font, anchor=CENTER)
        self.mainFrame.create_text(w + f, h - f, tags='texto', text=self.textos[1], font=font, anchor=CENTER, fill='white')

    
    def _quit(self, event):
        self._cleanMF()
        self.main_frame()


    def _buttons(self, width, height):
        w = width * 0.5
        h = height * 0.3
        d = 75
        for n_btn in range(len(self.buttons)):
            if self.buttons[n_btn] in self.__dict__ : self.__dict__[self.buttons[n_btn]].place(x=w, y=h + (d*n_btn), anchor=CENTER)

            
    def _open(self, btn, w=False, h=False):
        if type(btn) != str:
            for key in self.menuButtons:
                if str(self.__dict__[key]) == btn.widget.__dict__['_w']: 
                    btn = key
                    break

        if not w: w = self.current_width
        if not h: h = self.current_height
        font = self.text_font.copy()
        font[1] = f'{int(float(self.text_font[1]) * (w / self.width))}'
        exec(f'self.return_exec = {btn.upper()}')

        self._cleanMF()

        if self.mainFrame.children != {}:
            to_kill = list(self.mainFrame.children.values())[0]
            to_kill.destroy()

        scroll = Scrollbar(self.mainFrame, width=w * 0.01)
        scroll.pack(side=RIGHT, fill=Y, pady=h * 0.1, padx=w * 0.0075)

        button = Text(self.mainFrame, font=font, padx=w*0.025, pady=h*0.025, yscrollcommand=scroll.set)
        button.insert(END, self.return_exec)
        button['state'] = 'disabled'
        button.place(x=w*0.5, y=h*0.5, anchor=CENTER)
        self.__dict__[btn] = button


        self.quit = Button(self.mainFrame, font=self.subtitle_font, cursor='hand2', highlightthickness=0, anchor=CENTER)
        self.quit['text'] = 'Salir'
        self.quit.place(x=w*0.9, y=h*0.9, anchor=CENTER)
        self.quit.bind('<ButtonPress>', self._quit)      


    def __open_board(self, _):
        self.launcher.destroy()
        import chess.assets.test
        #self.main_frame()

        
