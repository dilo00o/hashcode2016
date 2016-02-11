class Outputer:
    def __init__(self):
        self.commands = []

    def load(self, drone, warehouse, product, quantity):
        self.commands.append("%s L %s %s %s" % (drone.id, warehouse.id, product, quantity))
        print(self.commands[-1])

    def deliver(self, drone, order, product, quantity):
        self.commands.append("%s D %s %s %s" % (drone.id, order, product, quantity))
        print(self.commands[-1])

    def wait(self, drone, steps):
        self.commands.append("%s W %s" % (drone.id, steps))
        print(self.commands[-1])

    def __str__(self):
        return "%s\n%s" % (len(self.commands), '\n'.join(self.commands))
