from game_of_life.src.game_of_life.main import Board


def test_create_board():
    test_board = Board(3, 3)
    assert str(test_board) == "...\n...\n...\n"


def test_place_cell():
    test_board = Board(3, 3)
    for j in range(3):
        test_board.place_cell(j, 1)
    assert str(test_board) == ".o.\n.o.\n.o.\n"

    test_board1 = Board(3, 3)
    for j in range(3):
        test_board1.place_cell(1, j)
    assert str(test_board1) == "...\nooo\n...\n"


def test_will_be_alive():
    test_board = Board(3, 3)
    for j in range(3):
        test_board.place_cell(1, j)
    assert test_board.will_be_alive(test_board.board, 1, 1)


def test_is_alive():
    test_board = Board(3, 3)
    for j in range(3):
        test_board.place_cell(j, 1)
    assert test_board.is_alive(1, 1)
    assert not test_board.is_alive(1, 0)
