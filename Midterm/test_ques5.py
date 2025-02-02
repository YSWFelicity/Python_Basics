from ques5 import name_processor


def test_name_processor():
    assert(name_processor(["Pele"]) == ["Pele"])
    assert(name_processor(["Sarah Jessica Parker"]) == ["Parker, Sarah"])
    assert(name_processor(["Darth Vader"]) == ["Vader, Darth"])
    assert(name_processor(["Pele", "Sarah Jessica Parker", "Darth Vader"]) == ["Pele", "Parker, Sarah", "Vader, Darth"])