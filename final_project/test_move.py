'''
Yingshu Wang
CS 5001, Fall 2021

Final project
'''


from move import Move


def test_constructor():
    move = Move([0, 0], [2, 2], True)
    assert(move.start == [0, 0])
    assert(move.end == [2, 2])
    assert(move.is_capturing_move is True)
    assert(move.captured_piece == [])
