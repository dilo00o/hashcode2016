from item import Items

class Warehouse:
    def __init__(self, warehouse_data):
        self.locX, self.locY, stocks = warehouse_data
        self.stocks = Items(stocks)

    def charge(self, drone):
        for i in drones.needed:
            charge = self.stocks.charge(drone.needed[i], i))
            drone.loaded[i] += charge
            drone.needed[i] -= charge
