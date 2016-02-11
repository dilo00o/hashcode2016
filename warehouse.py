from item import Items

class Warehouse:
    def __init__(self, warehouse_data, id):
        self.locX, self.locY, self.stocks = warehouse_data
        self.id = id

    def charge(self, drone, item_id, quantity=1):
        drone.load(item_id, quantity)
        self.stocks[item_id] -= quantity

    def has_item(self, item_id):
        return self.stocks[item_id] > 0
