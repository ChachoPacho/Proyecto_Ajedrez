from sys import path
from chess.constants import SAVES, BIN, os
import pickle
import time


class Config():
    def __init__(self) -> None:
        self.data = dict()
        self.dirs = ['game', 'gameboard', 'images_data']


    def save_game(self, name:str) -> None:
        name = name.replace(' ', '_')
        name = name.replace('\n', '')
        name = name.replace('/', '-')

        for data_dir in self.dirs:
            with open(BIN + data_dir, 'rb') as rfile: self.data.update({data_dir: pickle.load(rfile)})

        with open(SAVES + name, 'wb') as wfile:
            pickle.dump(self, wfile)
    

    @property
    def list_games(self):
        for save in os.scandir(SAVES):
            yield [save.name, time.ctime(save.stat().st_mtime)]


    def load_game(self, name):
        with open(SAVES + name, 'rb') as rfile: data = pickle.load(rfile)
        for name in data.__dict__: self.__setattr__(name, data.__dict__[name])

        for data_dir in self.dirs:
            with open(BIN + data_dir, 'wb') as wfile: pickle.dump(self.data[data_dir], wfile)

    
    def delete_game(self, name):
        os.remove(SAVES + name)
