from pysnake.game import move_snake, next_action, Direction


# Moves
def test_move_WEST() -> None:
    snake = [(1, 1)]
    snake = list(move_snake(snake, Direction.WEST))
    assert snake == [(0, 1)]

    snake = [(1, 0), (2, 0), (3, 0)]
    snake = list(move_snake(snake, Direction.WEST))
    assert snake == [(0, 0), (1, 0), (2, 0)]

    snake = [
        (1, 0), (2, 0),
                (2, 2), (3, 2),
                        (3, 3), (4, 3), (5, 3),
                                        (5, 4)
    ]

    snake = list(move_snake(snake, Direction.WEST))
    assert snake == [
        (0, 0), (1, 0), (2, 0),
                (2, 2), (3, 2),
                        (3, 3), (4, 3), (5, 3)
    ]


def test_move_EAST() -> None:
    snake = [(1, 1)]
    snake = list(move_snake(snake, Direction.EAST))
    assert snake == [(2, 1)]

    snake = [(3, 0), (2, 0), (1, 0)]
    snake = list(move_snake(snake, Direction.EAST))
    assert snake == [(4, 0), (3, 0), (2, 0)]

    snake = [
        (1, 0),
        (1, 1), (2, 1), (3, 1),
                        (3, 2), (4, 2), (5, 2),
                                        (5, 3)
    ]

    snake = list(move_snake(snake, Direction.EAST))
    assert snake == [
        (2, 0), (1, 0),
        (1, 1), (2, 1), (3, 1),
                        (3, 2), (4, 2), (5, 2)
    ]


def test_move_NORTH() -> None:
    snake = [(1, 1)]
    snake = list(move_snake(snake, Direction.NORTH))
    assert snake == [(1, 0)]

    snake = [(3, 1), (2, 1), (1, 1)]
    snake = list(move_snake(snake, Direction.NORTH))
    assert snake == [(3, 0), (3, 1), (2, 1)]

    snake = [
        (1, 1),
        (1, 2), (2, 2), (3, 2),
                        (3, 3), (4, 3), (5, 3),
                                        (5, 4)
    ]

    snake = list(move_snake(snake, Direction.NORTH))
    assert snake == [
        (1, 0),
        (1, 1),
        (1, 2), (2, 2), (3, 2),
                        (3, 3), (4, 3), (5, 3),
    ]


def test_move_SOUTH() -> None:
    snake = [(1, 1)]
    snake = list(move_snake(snake, Direction.SOUTH))
    assert snake == [(1, 2)]

    snake = [(3, 1), (2, 1), (1, 1)]
    snake = list(move_snake(snake, Direction.SOUTH))
    assert snake == [(3, 2), (3, 1), (2, 1)]

    snake = [
        (0, 1), (1, 1),
                (1, 2), (2, 2), (3, 2),
                                (3, 3), (4, 3), (5, 3),
                                                (5, 4)
    ]

    snake = list(move_snake(snake, Direction.SOUTH))
    assert snake == [
        (0, 2), (0, 1), (1, 1),
                (1, 2), (2, 2), (3, 2),
                                (3, 3), (4, 3), (5, 3),
    ]


# action
def test_next_action():
    action = next_action(snake, board, food, Direction.NORTH)
