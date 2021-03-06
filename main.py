from warehouse import Warehouse
from drones import Drone
from instructions_parser import parse
from collections import defaultdict
from outputter import Outputer
from math import ceil, sqrt

def main(file):
    with open(file) as handler:
        d = parse(handler)

    warehouses = [Warehouse(w,i) for i,w in enumerate(d['warehouses'])]
    WEIGHTS = d['products_weights']
    Drone.WEIGHTS = WEIGHTS
    raw_orders = d['orders']
    orders = []
    drones = [Drone(i, d['max_load']) for i in range(d['drone_number'])]
    output = Outputer()

    for order_id, order in enumerate(raw_orders):
        x, y, items = order
        weight = 0
        used_items = []
        for item in items:
            if weight + WEIGHTS[item] >= d['max_load']:
                orders.append((order_id, (x, y, used_items)))
                used_items = []
                weight = 0

            weight += WEIGHTS[item]
            used_items.append(item)
        if used_items:
            orders.append((order_id, (x, y, used_items)))

    for step in range(d['deadline']):
        list(map(lambda x: x.step(), drones))


        available_drones = list(filter(lambda x: not x.is_occupied, drones))
        if not orders:
            break

        while available_drones:
            if not orders:
                break
            order_id, order = orders.pop()
            destX, destY, order_products = order
            def dist(warehouse):
                d = ceil(sqrt((warehouse.locX - destX)**2 + (warehouse.locY - destY)**2))
                return (d, warehouse)

            sorted_warehouses = sorted(map(dist, warehouses), key=lambda x: x[0])
            drone = available_drones.pop()
            got_items = [False] * len(order_products)
            stack = []
            for dist, warehouse in sorted_warehouses:
                used = False
                for i, item in enumerate(order_products):
                    if got_items[i]:
                        continue
                    if warehouse.has_item(item):
                        warehouse.charge(drone, item)
                        got_items[i] = True
                        used = True
                        stack.append((warehouse, item))
                if all(got_items):
                    stack = reversed(stack)
                    for inst in stack:
                        drone.goto(inst[0].locX, inst[0].locY)
                        output.load(drone, inst[0], inst[1], 1)
                    drone.goto(destX, destY)
                    drone.unload()
                    for item in order_products:
                        output.deliver(drone, order_id, item, 1)
                    break

    return output


if __name__ == '__main__':
    open("busy_day.sol", "w").write(str(main('busy_day.in')))
    open("mother_of_all_warehouses.sol", "w").write(str(main('mother_of_all_warehouses.in')))
    open("redundancy.sol", "w").write(str(main('redundancy.in')))
