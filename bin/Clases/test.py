import pickle
from Game import Game

Game('white')

with open('bin/game', 'rb') as cache:
    xd = pickle.load(cache)

print(xd.turn)
