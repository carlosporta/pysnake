from itertools import product

from pysnake import func


def test_free_positions():
    state = func.initial_state(3, 3)
    state.snake.body = ((0, 0), (0, 1), (0, 2), (1, 2))
    state.food = (1, 0)
    assert sorted(func.free_positions(state)) == sorted(((1, 1), (2, 0), (2, 1), (2, 2)))


def test_calculate_new_IJ():
    origen = (0, 1)
    direction = (0, 1)
    assert func.calculate_new_IJ(origen, direction) == (0, 2)

    origen = (0, 1)
    direction = (2, 3)
    assert func.calculate_new_IJ(origen, direction) == (2, 4)


def test_is_out_of_bounds():
    state = func.initial_state(4, 5)
    positions = product(range(state.rows), range(state.cols))

    for p in positions:
        state.snake.body = (p,)
        assert not func.is_out_of_bounds(p, state)

    assert func.is_out_of_bounds((4, 4), state)
    assert func.is_out_of_bounds((-1, -1), state)
    assert func.is_out_of_bounds((2, -1), state)
    assert func.is_out_of_bounds((5, 0), state)


def test_snake_head():
    state = func.initial_state(3, 2)
    state.snake.body = ((0, 0), (0, 1), (0, 2), (1, 2))
    assert func.snake_head(state) == (0, 0)


def test_next_snake_head():
    state = func.initial_state(3, 4)
    state.snake.body = ((0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = func.Directions.SOUTH
    assert func.next_snake_head(state) == (1, 0)

    state.snake.body = ((1, 1), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = func.Directions.NORTH
    assert func.next_snake_head(state) == (0, 1)


def test_next_snake_tail():
    state = func.initial_state(3, 4)
    state.snake.body = ((0, 1), (0, 2), (1, 2))
    state.snake.direction = func.Directions.WEST
    assert func.next_snake_tail(state) == ((0, 1), (0, 2))

    state.snake.body = ((1, 1), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = func.Directions.EAST
    assert func.next_snake_tail(state) == ((1, 1), (0, 0), (0, 1), (0, 2))


def test_next_snake():
    state = func.initial_state(3, 4)
    state.snake.body = ((1, 0), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = func.Directions.EAST
    assert func.next_snake(state).body == ((1, 1), (1, 0), (0, 0), (0, 1),
                                           (0, 2))

    state.snake.body = ((1, 1), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = func.Directions.SOUTH
    assert func.next_snake(state).body == ((2, 1), (1, 1), (0, 0), (0, 1),
                                           (0, 2))


def test_move_WEST():
    state = func.initial_state(4, 4)
    state.snake.body = ((0, 1),)
    state.snake.direction = func.Directions.WEST
    state = func.move_snake(state)
    assert state.snake.body == ((0, 0),)

    state.snake.body = ((0, 1), (0, 2), (0, 3))
    state = func.move_snake(state)
    assert state.snake.body == ((0, 0), (0, 1), (0, 2))


def test_move_EAST():
    state = func.initial_state(6, 12)
    state.snake.body = ((0, 1),)
    state.snake.direction = func.Directions.EAST
    state = func.move_snake(state)
    assert state.snake.body == ((0, 2),)

    state.snake.body = ((1, 1), (0, 1), (0, 2))
    state = func.move_snake(state)
    assert state.snake.body == ((1, 2), (1, 1), (0, 1))


def test_move_NORTH():
    state = func.initial_state(4, 4)
    state.snake.body = ((1, 1),)
    state.snake.direction = func.Directions.NORTH
    state = func.move_snake(state)
    assert state.snake.body == ((0, 1),)

    state.snake.body = ((1, 0), (1, 1), (0, 1), (0, 2))
    state = func.move_snake(state)
    assert state.snake.body == ((0, 0), (1, 0), (1, 1), (0, 1))


def test_move_SOUTH():
    state = func.initial_state(3, 10)
    state.snake.body = ((1, 1),)
    state.snake.direction = func.Directions.SOUTH
    state = func.move_snake(state)
    assert state.snake.body == ((2, 1),)

    state.snake.body = ((1, 0), (1, 1), (0, 1), (0, 2))
    state = func.move_snake(state)
    assert state.snake.body == ((2, 0), (1, 0), (1, 1), (0, 1))


def test_eat():
    state = func.initial_state(3, 3)
    state.snake.body = ((0, 0),)
    state.food = (0, 1)
    state = func.eat(state)
    assert state.snake.body == ((0, 1), (0, 0))


def test_next_state():
    # eat
    state = func.initial_state(3, 5)
    state.snake.body = ((0, 0),)
    state.food = (0, 1)
    state = func.next_state(state)
    assert state.snake.body == ((0, 1), (0, 0))

    # move
    state = func.initial_state(3, 5)
    state.snake.body = ((0, 2), (0, 1), (0, 0))
    state.food = (0, 4)
    state = func.next_state(state)
    assert state.snake.body == ((0, 3), (0, 2), (0, 1))

    # out_of_bounds = None
    state = func.initial_state(1, 1)
    state.snake.body = ((0, 0),)

    state.snake.direction = func.Directions.EAST
    assert func.next_state(state) is None

    state.snake.direction = func.Directions.NORTH
    assert func.next_state(state) is None

    state.snake.direction = func.Directions.SOUTH
    assert func.next_state(state) is None

    state.snake.direction = func.Directions.WEST
    assert func.next_state(state) is None
