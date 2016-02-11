from warehouse import Warehouse
from drones import Drone
from instructions_parser import parse
from collections import defaultdict

def main(file):
    with open(file) as handler:
        d = parse(handler)

    warehouses = [Warehouse(w,i) for i,w in enumerate(d['warehouses'])]
    WEIGHTS = d['products_weights']
    raw_orders = d['orders']
    orders = []
    drones = [Drone(i, items) for i in range(d['drone_number'])]
    output = Outputter()

    for order_id, order in enumerate(raw_orders):
        x, y, items = order
        weight = 0
        used_items = []
        for item in items:
            if weight + WEIGHTS[item] > d['orders']:
                orders.append((order_id, used_items))
                used_items = []
                weight = 0
            else:
                weight += WEIGHTS[item]
                used_items.append(item)



    for step in range(d['deadline']):
        map(lambda x: x.step(), drones)
        available_drones = list(filter(lambda x: not x.is_occupied()))

        for order_id, order in orders:
            destX, destY, order_products = order

            def dist(warehouse):
                d = ceil(sqrt((warehouse.locX - destX)**2 + (warehouse.locY - destY)**2))
                return (d, warehouse)

            sorted_warehouses = sorted(map(dist, warehouses), key=lambda x: x[0])

            if available_drones:
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
                            stack.append((warehouse.id, warehouse.locX, warehouse.locY))
                    if all(got_items):
                        stack = reversed(stack)
                        for instruction in stack:
                            drone.goto(instruction[1], instruction[2])
                            output.load(drone, order_id, item, 1)
                        drone.goto(destX, destY)
                        drone.unload()
                        break
