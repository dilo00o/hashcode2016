from warehouse import Warehouse
from drones import Drone
from instructions_parser import parse

def main(file):
    with open(file) as handler:
        d = parse(handler)

    warehouses = [Warehouse(w) for w in d['warehouses']]
    drones = [Drone(i, d['max_load'], len(d['products_weights'])) for i in range(d['drone_number'])]

    for i in range(d['deadline']):
        pass
