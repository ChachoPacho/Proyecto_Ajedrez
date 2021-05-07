import pickle

class Hola():
    def __init__(self, color):
        self.color = color
        self.hola = "Hola"

    def Message(self):
        string = self.hola + " " + str(self.color)
        print(string)
        self.msg = string

    def Save(self):
        with open("test", "wb") as op:
            pickle.dump(self, op)


def Load():
    with open("test", "rb") as op:
        return pickle.load(op)


if __name__ == "__main__":
    cls = Hola('verde')
    cls.Message()
    cls = Load()
    cls.Message()
    
