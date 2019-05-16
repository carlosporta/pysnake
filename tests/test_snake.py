from pysnake.game import move, eat, next_action, Direction


# Moves
def test_move_WEST() -> None:
    snake = ((1, 1),)
    snake = move(snake, Direction.WEST)
    assert snake == ((0, 1),)

    snake = ((1, 0), (2, 0), (3, 0))
    snake = move(snake, Direction.WEST)
    assert snake == ((0, 0), (1, 0), (2, 0))


def test_move_EAST() -> None:
    snake = ((1, 1),)
    snake = move(snake, Direction.EAST)
    assert snake == ((2, 1),)

    snake = ((3, 0), (2, 0), (1, 0))
    snake = move(snake, Direction.EAST)
    assert snake == ((4, 0), (3, 0), (2, 0))


def test_move_NORTH() -> None:
    snake = ((1, 1),)
    snake = move(snake, Direction.NORTH)
    assert snake == ((1, 0),)

    snake = ((3, 1), (2, 1), (1, 1))
    snake = move(snake, Direction.NORTH)
    assert snake == ((3, 0), (3, 1), (2, 1))


def test_move_SOUTH() -> None:
    snake = ((1, 1),)
    snake = move(snake, Direction.SOUTH)
    assert snake == ((1, 2),)

    snake = ((3, 1), (2, 1), (1, 1))
    snake = move(snake, Direction.SOUTH)
    assert snake == ((3, 2), (3, 1), (2, 1))


# Eat
def test_eat():
    snake = ((1, 1),)
    snake = eat(snake, (0, 1))
    assert snake == ((0, 1), (1, 1))

    snake = ((1, 0), (2, 0), (3, 0))
    snake = eat(snake, (1, 1))
    assert snake == ((1, 1), (1, 0), (2, 0), (3, 0))


# Next Action
def test_next_action_must_be_move():
    snake = ((1, 1),)
    food = (2, 1)
    action = next_action(snake, food, Direction.WEST, (10, 10))
    assert action is 'move'


def test_next_action_must_be_eat():
    snake = ((2, 1),)
    food = (2, 0)
    action = next_action(snake, food, Direction.NORTH, (10, 10))
    assert action is 'eat'


def test_next_action_must_be_out_of_bounds():
    snake = ((2, 0),)
    food = (2, 2)
    action = next_action(snake, food, Direction.NORTH, (10, 10))
    assert action is 'out_of_bounds'


def test_next_action_must_be_self_collision():
    snake = ((1, 0), (2, 0))
    food = (2, 3)
    action = next_action(snake, food, Direction.EAST, (10, 10))
    assert action is 'self_collision'
