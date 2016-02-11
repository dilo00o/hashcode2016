from math import ceil, sqrt

class Drone:
    def __init__(self, id, weight_carried, item_available):
        self.id = id
        self.posX, self.posY = 0, 0
        self.weight_carried = weight_carried
        self.turns = 0
        self.needed = [0 for i in range(item_available)]
        self.loaded = [0 for i in range(item_available)]

    def fetch(self, posX, posY):
        self.turns += shortest_path(posX, posY, self.posX, self.posY)
        self.posX = posX
        self.posY = posY

    def load(self, item, warehouse):
        warehouse.charge(self)



def shortest_path(ra, ca, rb, cb):
    return ceil(sqrt(abs(ra - rb)**2 + abs(ca - cb)**2))
