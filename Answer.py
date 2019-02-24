class Piece:

    def __init__(self, xs, ys, xe, ye):
        self.xs = xs
        self.ys = ys
        self.xe = xe
        self.ye = ye

    def __str__(self):
        return ' '.join(map(str, [self.xs, self.ys, self.xe, self.ye]))

class Answer:

    def __init__(self):
        self.all = []

    def put(self, new):
        p = Piece(*new)
        self.all.append(p)

    def __str__(self):
        s = str(len(self.all)) + '\n'
        for x in self.all:
            s += str(x) + '\n'
        return s

    def clear(self):
        self.all = []

