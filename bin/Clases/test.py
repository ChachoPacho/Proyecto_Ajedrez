
import sys

sys.path.append("..")
from Clases.game import Game
from moves import Movements

xd = Game()
xd.start('white')
print(xd.board)