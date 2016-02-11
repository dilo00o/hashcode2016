from math import ceil, sqrt
from item import Items

class drone:
    def __init__(self, weight_carried):
        self.posX, self.posY = 0, 0
        self.weight_carried = weight_carried
        self.turns = 0
        self.needed = Items()
        self.loaded = Items()

    def fetch(self, posX, posY):
        self.turns += shortest_path(posX, posY, self.posX, self.posY)
        self.posX = posX
        self.posY = posY

    def load(self, item):



def shortest_path(ra, ca, rb, cb):
    return ceil(sqrt(abs(ra - rb)**2 + abs(ca - cb)**2))
