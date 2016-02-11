from math import ceil, sqrt

class Drone:
    def __init__(self, id, max_weight):
        self.id = id
        self.posX, self.posY = 0, 0
        self.max_weight = max_weight
        self.turns = 0
        self.carried = []

    def goto(self, posX, posY):
        self.turns += shortest_path(posX, posY, self.posX, self.posY)
        self.posX = posX
        self.posY = posY

    def load(self, item_id, quantity=1):
        if self.weight + WEIGHTS[item_id] * quantity > self.max_weight:
            raise Exeption("No more space")
        self.carried += [item_id] * quantity
        self.turns += 1

    def unload(self):
        self.carried = []
        self.turns += 1

    def step(self):
        if self.turns > 0:
            self.turns -= 1

    @property
    def is_occupied(self):
        return bool(self.turns)


    @property
    def weight(self):
        return sum(map(lambda x: WEIGHTS[x], self.carried))



def shortest_path(ra, ca, rb, cb):
    return ceil(sqrt(abs(ra - rb)**2 + abs(ca - cb)**2))
