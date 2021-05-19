from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#   Creates the window where the interface will be
class Launcher:
    launcher = Tk()
    launcher.columnconfigure(0, weight=1)
    launcher.rowconfigure(0, weight=1)

    def __init__(self, window_name):
        self.launcher.title(window_name)
        self.font = ('Helvetica', 15)
        self._menu()
        self._prepare_window()
        self._prepare_frame()


    def donothing(self):
        filewin = Toplevel(self.launcher)
        button = Button(filewin, text="Do nothing button")
        button.pack()


    def _menu(self):
        menu = Menu(self.launcher, font= self.font)
        menu.add_command(label="New", command=self.donothing)
        menu.add_command(label="Open", command=self.donothing)
        menu.add_command(label="Save", command=self.donothing)
        menu.add_command(label="Save as...", command=self.donothing)
        menu.add_command(label="Close", command=self.donothing)
        self.launcher.config(menu = menu)


    def _prepare_window(self):
        self.width = 480
        self.height = 320
        self.launcher.geometry(f'{self.width}x{self.height}')

    
    def _prepare_frame(self):
        #   main_frame creation, where all will be included
        

        self.image = Image.open("./src/backgrounds/chessboard.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.main_frame = Label(self.launcher, image=self.background_image)
        self.main_frame.grid(row=0, column=0, sticky=NSEW)
        self.main_frame.rowconfigure([0], weight=1)
        self.main_frame.columnconfigure([0], weight=1)
        self.main_frame.bind('<Configure>', self.__resize_image)


        
    def __resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.main_frame.configure(image =  self.background_image)



    def start(self):
        self.launcher.mainloop()

    
    def stop(self):
        self.launcher.destroy()
