from icecream import IceCream


def test_Constructor():
    icecream = IceCream("chocolate", 2.5)
    assert(icecream.flavor == "chocolate")
    assert(icecream.price_per_scoop == 2.5)


def test_get_cost():
    icecream = IceCream("chocolate", 4)
    assert(icecream.get_cost(3) == 12)
    assert(icecream.get_cost(1) == 8)
    assert(icecream.get_cost(11) == 42)
    assert(icecream.get_cost(2) == 8)
    assert(icecream.get_cost(10) == 40)
