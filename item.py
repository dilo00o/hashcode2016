

class Items:
    def __init__(self, items_weights):
        self.weights = items_weights
        self.possessed = [0 for i in range(len(items_weights))]

    def charge(self, many, order):
        charging = max(self.possessed[order], many)
        self.possessed[order] -= charging
        return (charging, self.weights[order] * charging)
