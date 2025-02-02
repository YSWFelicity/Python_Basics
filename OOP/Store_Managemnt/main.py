class Item:
    def __init__(self, name):
        print(f"An instance created: {name}")
        self.name = name
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone")
item1.name = "Phone"
item1.price = 100
item1.quantity = 5


item2 = Item("Laptop")
item2.name = "Laptop"
item2.price = 1000
item2.quantit = 3
