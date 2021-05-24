from chess.constants import BIN, SRC
from PIL import Image, ImageTk
import json
import pickle


class Data():
    def __init__(self):
        with open(BIN + '/data.json', 'r') as outfile: data = json.load(outfile)

        for name in data: self.__setattr__(name, data[name])


class Images():
    def __init__(self, srcDir, width=False, height=False):
        self.data = Data().element
        self.srcDir = srcDir
        self.width = width
        self.height = height


    @property
    def get(self):
        re_list = {}
        for image in Data().element[self.srcDir]:
            _image = Image.open(SRC + self.srcDir + '/' + image + '.png')
            if self.width: _image = _image.resize((int(self.width), int(self.height)), Image.ANTIALIAS)
            _image = ImageTk.PhotoImage(_image)
            re_list.update({image: _image})

        return re_list


class Images_Data():
    def __init__(self):
        try:
            with open(BIN + 'images_data', 'rb') as rfile: data = pickle.load(rfile)

            for name in data.__dict__: self.__setattr__(name, data.__dict__[name])

        except:
            self.pos = []
            self.pieces = []


    def __setattr__(self, name, value):
        self.__dict__[name] = value
        self.__save()


    def append(self, piece):
        self.pos.append(piece)
        self.pieces.append(piece)


    def update(self, posI, posF):
        self.pos[self.pos.index(posI)] = posF


    def delete(self, pos):
        index = self.pos.index(pos)
        self.pos.pop(index)
        self.pieces.pop(index)


    def select(self, pos):
        return self.pieces[self.pos.index(pos)]


    def reset(self):
        self.pos.clear()
        self.pieces.clear()


    def __save(self):
        with open(BIN + 'images_data', 'wb') as wfile:
            pickle.dump(self, wfile)
