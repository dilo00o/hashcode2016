def parse(stream):
    row, col, drone_number, deadline, max_load = list(map(int, stream.readline().strip().split()))
    product_types_len = int(stream.readline().strip())
    products_weights = list(map(int, stream.readline().strip().split()))

    warehouses_len = int(stream.readline().strip())
    warehouses = []
    for _ in range(warehouses_len):
        x, y = list(map(int, stream.readline().strip().split()))
        quantity_per_product = list(map(int, stream.readline().strip().split()))
        warehouses.append((x, y, quantity_per_product))

    orders_len = int(stream.readline().strip())
    orders = []
    for _ in range(orders_len):
        x, y = list(map(int, stream.readline().strip().split()))
        order_size = int(stream.readline().strip())
        product_types = list(map(int, stream.readline().strip().split()))
        orders.append((x,y, product_types))

    return {
        'grid': (row, col),
        'drone_number': drone_number,
        'deadline': deadline,
        'max_load': max_load,
        'products_weights': products_weights,
        'warehouses': warehouses,
        'orders': orders,
    }
