


class Mobile:
    # STATE
    def __init__(self, mid, brand, cost, color):
        self.mid = mid
        self.brand = brand
        self.cost = cost
        self.color = color

    # BEHAVIOR
    def get_mobileinfo(self):
        print("Mobile information: ", self.mid, self.brand, self.cost, self.color)

# Object creation: Initializing State
samsung = Mobile(100, "Samsung S23", 100000, "Black")

# Getting Behavior
samsung.get_mobileinfo()