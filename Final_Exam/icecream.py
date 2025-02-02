class IceCream:
    def __init__(self, flavor, price_per_scoop):
        self.flavor = flavor
        self.price_per_scoop = price_per_scoop

    def get_cost(self, number_of_scoop):
        scoop_min = 2
        scoop_max = 10
        discount = 2
        cost = number_of_scoop * self.price_per_scoop
        if number_of_scoop < scoop_min:
            cost = scoop_min * self.price_per_scoop
        elif number_of_scoop > scoop_max:
            cost = cost - discount
        return cost
