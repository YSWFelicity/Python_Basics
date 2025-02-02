from ques4 import get_ticket_cost


def test_get_ticket_cost():
    assert(get_ticket_cost([10, 39, 40]) == 50.0)
