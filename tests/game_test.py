from itertools import product

from pysnake import game


def test_free_positions():
    state = game.initial_state(3, 3)
    state.snake.body = ((0, 0), (0, 1), (0, 2), (1, 2))
    state.food = (1, 0)

    positions = sorted(game.free_positions(state))
    assert positions == sorted(((1, 1), (2, 0), (2, 1), (2, 2)))


def test_calculate_new_IJ():
    origen = (0, 1)
    direction = (0, 1)
    assert game.calculate_new_IJ(origen, direction) == (0, 2)

    origen = (0, 1)
    direction = (2, 3)
    assert game.calculate_new_IJ(origen, direction) == (2, 4)


def test_is_out_of_bounds():
    state = game.initial_state(4, 5)
    positions = product(range(state.rows), range(state.cols))

    for p in positions:
        state.snake.body = (p,)
        assert not game.is_out_of_bounds(p, state)

    assert game.is_out_of_bounds((4, 4), state)
    assert game.is_out_of_bounds((-1, -1), state)
    assert game.is_out_of_bounds((2, -1), state)
    assert game.is_out_of_bounds((5, 0), state)


def test_snake_head():
    state = game.initial_state(3, 2)
    state.snake.body = ((0, 0), (0, 1), (0, 2), (1, 2))
    assert game.snake_head(state) == (0, 0)


def test_next_snake_head():
    state = game.initial_state(3, 4)
    state.snake.body = ((0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = game.Directions.SOUTH
    assert game.next_snake_head(state) == (1, 0)

    state.snake.body = ((1, 1), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = game.Directions.NORTH
    assert game.next_snake_head(state) == (0, 1)


def test_next_snake_tail():
    state = game.initial_state(3, 4)
    state.snake.body = ((0, 1), (0, 2), (1, 2))
    state.snake.direction = game.Directions.WEST
    assert game.next_snake_tail(state) == ((0, 1), (0, 2))

    state.snake.body = ((1, 1), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = game.Directions.EAST
    assert game.next_snake_tail(state) == ((1, 1), (0, 0), (0, 1), (0, 2))


def test_next_snake():
    state = game.initial_state(3, 4)
    state.snake.body = ((1, 0), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = game.Directions.EAST
    assert game.next_snake(state).body == ((1, 1), (1, 0), (0, 0), (0, 1),
                                           (0, 2))

    state.snake.body = ((1, 1), (0, 0), (0, 1), (0, 2), (1, 2))
    state.snake.direction = game.Directions.SOUTH
    assert game.next_snake(state).body == ((2, 1), (1, 1), (0, 0), (0, 1),
                                           (0, 2))


def test_move_WEST():
    state = game.initial_state(4, 4)
    state.snake.body = ((0, 1),)
    state.snake.direction = game.Directions.WEST
    state = game.move_snake(state)
    assert state.snake.body == ((0, 0),)

    state.snake.body = ((0, 1), (0, 2), (0, 3))
    state = game.move_snake(state)
    assert state.snake.body == ((0, 0), (0, 1), (0, 2))


def test_move_EAST():
    state = game.initial_state(6, 12)
    state.snake.body = ((0, 1),)
    state.snake.direction = game.Directions.EAST
    state = game.move_snake(state)
    assert state.snake.body == ((0, 2),)

    state.snake.body = ((1, 1), (0, 1), (0, 2))
    state = game.move_snake(state)
    assert state.snake.body == ((1, 2), (1, 1), (0, 1))


def test_move_NORTH():
    state = game.initial_state(4, 4)
    state.snake.body = ((1, 1),)
    state.snake.direction = game.Directions.NORTH
    state = game.move_snake(state)
    assert state.snake.body == ((0, 1),)

    state.snake.body = ((1, 0), (1, 1), (0, 1), (0, 2))
    state = game.move_snake(state)
    assert state.snake.body == ((0, 0), (1, 0), (1, 1), (0, 1))


def test_move_SOUTH():
    state = game.initial_state(3, 10)
    state.snake.body = ((1, 1),)
    state.snake.direction = game.Directions.SOUTH
    state = game.move_snake(state)
    assert state.snake.body == ((2, 1),)

    state.snake.body = ((1, 0), (1, 1), (0, 1), (0, 2))
    state = game.move_snake(state)
    assert state.snake.body == ((2, 0), (1, 0), (1, 1), (0, 1))


def test_eat():
    state = game.initial_state(3, 3)
    state.snake.body = ((0, 0),)
    state.food = (0, 1)
    state = game.eat(state)
    assert state.snake.body == ((0, 1), (0, 0))


def test_next_state():
    # eat
    state = game.initial_state(3, 5)
    state.snake.body = ((0, 0),)
    state.food = (0, 1)
    state = game.next_state(state)
    assert state.snake.body == ((0, 1), (0, 0))

    # move
    state = game.initial_state(3, 5)
    state.snake.body = ((0, 2), (0, 1), (0, 0))
    state.food = (0, 4)
    state = game.next_state(state)
    assert state.snake.body == ((0, 3), (0, 2), (0, 1))

    # out_of_bounds = None
    state = game.initial_state(1, 1)
    state.snake.body = ((0, 0),)

    state.snake.direction = game.Directions.EAST
    assert game.next_state(state) is None

    state.snake.direction = game.Directions.NORTH
    assert game.next_state(state) is None

    state.snake.direction = game.Directions.SOUTH
    assert game.next_state(state) is None

    state.snake.direction = game.Directions.WEST
    assert game.next_state(state) is None


def test_next_move_is_the_snake_tail():
    state = game.initial_state(6, 7)
    state.food = (3, 3)
    state.snake.direction = game.Directions.SOUTH
    state.snake.body = ((0, 0), (0, 1), (1, 1), (1, 0))

    state = game.next_state(state)
    assert state.snake.body == ((1, 0), (0, 0), (0, 1), (1, 1))

    state.snake.body = ((0, 0), (1, 0))
    state = game.next_state(state)
    assert state is None
