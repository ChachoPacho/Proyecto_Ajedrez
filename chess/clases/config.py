from sys import path
from chess.constants import SAVES, BIN, os
from chess.clases.game import Game
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
            try: 
                with open(BIN + data_dir, 'rb') as rfile: self.data.update({data_dir: pickle.load(rfile)})
            
            except: ''

        with open(SAVES + name, 'wb') as wfile: pickle.dump(self, wfile)


    @property
    def issaved(self) -> bool:
        b = os.path.isfile(BIN + 'save')
        if b:
            with open(BIN + 'save', 'rb') as rfile: name = pickle.load(rfile)
            self.save_game(name)

        return b


    @property
    def list_games(self):
        for save in os.scandir(SAVES):
            yield [save.name, time.ctime(save.stat().st_mtime)]


    def remove_save(self):
        if os.path.isfile(BIN + 'save'): os.remove(BIN + 'save')


    def load_game(self, name):
        self.remove_save()
        with open(SAVES + name, 'rb') as rfile: data = pickle.load(rfile)
        for dataName in data.__dict__: self.__setattr__(dataName, data.__dict__[dataName])

        for data_dir in self.dirs:
            with open(BIN + data_dir, 'wb') as wfile: pickle.dump(self.data[data_dir], wfile)

        with open(BIN + 'save', 'wb') as wfile: pickle.dump(name, wfile)


    def new_game(self, name, color):
        self.remove_save()
        Game().start(color)
        with open(BIN + 'save', 'wb') as wfile: pickle.dump(name, wfile)

    
    def delete_game(self, name):
        os.remove(SAVES + name)
