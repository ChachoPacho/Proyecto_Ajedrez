if __name__ == '__main__':
    from chess.assets.launcher import Launcher
    xd = Launcher()

else:
    from chess.assets.window import Window
    from chess.assets.board import Board

    xd = Window('xdxd')
    xd2 = Board(xd)
    xd2._board()
    xd.start()
