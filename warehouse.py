from item import Items

class Warehouse:
    def __init__(self, warehouse_data):
        self.locX, self.locY, self.stocks = warehouse_data

    def charge(self, drone, item_id, quantity=1):
        drone.load(item_id, quantity)
        self.stocks[item_id] -= quantity
