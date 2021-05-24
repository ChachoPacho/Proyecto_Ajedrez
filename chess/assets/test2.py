from main import Window
from board import Board
import sys

xd = Window('xdxd')
xd2 = Board(xd)
xd2._board()
xd.start()

# from launcher import Launcher
# xd = Launcher('xdxd')
# from tkinter import *

# launcher = Tk()
# launcher.columnconfigure(0, weight=1)
# launcher.rowconfigure(0, weight=1)
# launcher.title('xd')
# font = ('Helvetica', 15)

# launcher.geometry('480x320')
# launcher.rowconfigure([1], weight=0)
# launcher.rowconfigure([0], weight=1)



# #image = Image.open("./src/backgrounds/chessboard.jpg")
# #background_image = ImageTk.PhotoImage(image)
# bg = PhotoImage(file="chessboard.png")


# mainframe = Canvas(launcher, width=480, height=320)
# mainframe.pack(fill=BOTH, expand=TRUE)
# mainframe.create_image(0, 0, image = bg)


# launcher.mainloop()