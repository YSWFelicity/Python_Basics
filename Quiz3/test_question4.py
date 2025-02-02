from pytest import raises


def test_add_tip():
    with raises(ValueError):
        add_tip(30, 0)
    with raises(ValueError):
        add_tip(30, 1.1)
    with raises(ValueError):
        add_tip(30, "0")   