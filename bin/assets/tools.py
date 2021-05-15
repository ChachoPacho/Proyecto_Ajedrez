from PIL import Image, ImageTk
import json
import pickle
import os

cwd = os.path.dirname(__file__)


class Data():
    def __init__(self):
        with open(cwd + '/data.json', 'r') as outfile:
            data = json.load(outfile)

        for name in data:
            self.__setattr__(name, data[name])


class Images():
    def __init__(self):
        self.data = Data().element
        self.start()

    
    def start(self):
        def __resize(img_list):
            re_list = {}
            for image in img_list:
                _image = Image.open(cwd + '/' + self.data['dir'] + image + self.data['ext'])
                _image = ImageTk.PhotoImage(_image)
                re_list.update({image: _image})

            return re_list

        self.pieces = __resize(self.data['pieces'])
        self.special = __resize(self.data['special'])


    def resize(self, width):
        #   filter
        if width < 90:
            width = 90

        def __resize(img_list):
            re_list = {}
            for image in img_list:
                _image = Image.open(cwd + '/' + self.data['dir'] + image + self.data['ext'])
                _image = _image.resize((int(width), int(width)), Image.ANTIALIAS)
                _image = ImageTk.PhotoImage(_image)
                re_list.update({image: _image})

            return re_list

        self.pieces = __resize(self.data['pieces'])
        self.special = __resize(self.data['special'])


class Images_Data():
    def __init__(self):
        try:
            with open(cwd + '/bin/images_data', 'rb') as rfile:
                data = pickle.load(rfile)

            for name in data.__dict__:
                self.__setattr__(name, data.__dict__[name])

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
        with open(cwd + '/bin/images_data', 'wb') as wfile:
            pickle.dump(self, wfile)
