from quiz2 import ends_with_s


def test_ends_with_s():
    assert(ends_with_s("cats")) 
    assert(ends_with_s("") is False) 
    assert(ends_with_s("apple") is False) 
    assert(ends_with_s("S"))
