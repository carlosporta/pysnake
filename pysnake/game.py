from copy import deepcopy
from dataclasses import dataclass
from functools import wraps
from itertools import product
from random import choice
from typing import Tuple, NamedTuple, Callable, Any

# Data types
IJ = Tuple[int, int]
Food = IJ


@dataclass
class Snake:
    body: Tuple[IJ, ...]
    direction: IJ


@dataclass
class State:
    rows: int
    cols: int
    points: int
    snake: Snake
    food: Food


# Possible directions
class _direction(NamedTuple):
    NORTH: IJ = (-1, 0)
    SOUTH: IJ = (1, 0)
    WEST: IJ = (0, -1)
    EAST: IJ = (0, 1)


Directions = _direction()


def random_direction():
    return choice(Directions)


# Helpers
def deepcopy_params(f: Callable) -> Any:
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*(deepcopy(x) for x in args),
                 **{k: deepcopy(v) for k, v in kwargs.items()})
    return wrapper


# State
def initial_state(rows: int, cols: int) -> State:
    snake = Snake(((0, 0),), Directions.EAST)
    return State(rows, cols, 0, snake, (0, 0))


def random_state(rows: int, cols: int) -> State:
    state = initial_state(rows, cols)
    state.snake = Snake((random_empty_IJ(state),), random_direction())
    state.food = random_empty_IJ(state)
    return state


# Position
def free_positions(state: State) -> set:
    positions = product(range(state.rows), range(state.cols))
    free_options = set(positions) - set(state.snake.body) - set([state.food])
    return free_options


def random_empty_IJ(state: State) -> IJ:
    return choice(list(free_positions(state)))


def calculate_new_IJ(origen: IJ, direction: IJ) -> IJ:
    return tuple(sum(i) for i in zip(origen, direction))


def is_out_of_bounds(ij: IJ, state: State) -> bool:
    i, j = ij
    return not(-1 < i < state.rows and -1 < j < state.cols)


# Snake
def snake_head(state: State) -> IJ:
    return state.snake.body[0]


def snake_direction(state: State) -> IJ:
    return state.snake.direction


@deepcopy_params
def change_snake_direction(direction: IJ, state: State) -> State:
    state.snake.direction = direction
    return state


def next_snake_head(state: State) -> IJ:
    return calculate_new_IJ(snake_head(state), snake_direction(state))


def next_snake_tail(state: State) -> Tuple[IJ, ...]:
    return state.snake.body[:-1]


def next_snake(state: State) -> Snake:
    body = (next_snake_head(state),) + next_snake_tail(state)
    direction = state.snake.direction
    return Snake(body, direction)


@deepcopy_params
def move_snake(state: State) -> State:
    state.snake = next_snake(state)
    return state


@deepcopy_params
def eat(state: State) -> State:
    state.snake.body = (state.food,) + state.snake.body
    state.points += 1
    state.food = random_empty_IJ(state)
    return state


@deepcopy_params
def next_state(state: State) -> State:
    head = next_snake_head(state)
    if state.food == head:
        return eat(state)
    elif is_out_of_bounds(head, state) or head in state.snake.body[:-1]:
        return None
    else:
        return move_snake(state)
