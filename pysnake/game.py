from copy import deepcopy
from dataclasses import dataclass
from random import randint, choice
from typing import List, NamedTuple, Tuple, Union


# XY = Tuple[int, int]
# Snake = Iterable[XY]
# Food = Iterable[XY]

# _direction = namedtuple('Direction', 'NORTH SOUTH WEST EAST'.split())
# Direction = _direction(NORTH=(0, -1), SOUTH=(0, 1), WEST=(-1, 0), EAST=(1, 0))


# @dataclass
# class GameSate:
#     rows: int
#     cols: int
#     snake: Snake
#     food: Food
#     points: int
#     current_direction: XY


# def random_direction():
#     return choice(Direction)


# def empty_game_state(rows: int, cols: int) -> GameSate:
#     return GameSate(rows, cols, [], [], 0, [])


# def random_game_state(rows: int, cols: int) -> GameSate:
#     game_state = empty_game_state(rows, cols)

#     snake = init_snake(random_empty_xy(game_state))
#     game_state = add_snake(game_state, snake)

#     food = init_food(random_empty_xy(game_state))
#     game_state = add_food(game_state, food)

#     direction = random_direction()
#     game_state = add_direction(game_state, direction)

#     return game_state


# def add_snake(game_state: GameSate, snake: Snake) -> GameSate:
#     new_state = deepcopy(game_state)
#     new_state.snake = snake
#     return new_state


# def add_food(game_state: GameSate, food: Food) -> GameSate:
#     new_state = deepcopy(game_state)
#     new_state.food = food
#     return new_state


# def add_direction(game_state: GameSate, direction: XY) -> GameSate:
#     new_state = deepcopy(game_state)
#     new_state.current_direction = direction
#     return new_state


# def keep_going(game_state: GameSate):
#     return move(game_state, game_state.current_direction)


# def init_snake(xy: XY) -> Snake:
#     return [xy]


# def init_food(xy: XY) -> Food:
#     return xy


# def random_empty_xy(game_state: GameSate) -> XY:
#     while True:
#         xy = random_xy(game_state.rows, game_state.cols)
#         if xy == game_state.food or xy not in game_state.snake:
#             return xy


# def random_xy(rows: int, cols: int) -> XY:
#     return (randint(0, cols-1), randint(0, rows-1))


# def move(game_state: GameSate, xy: XY):
#     current_x, current_y = game_state.snake[0]
#     new_x, new_y = xy
#     new_xy = (current_x + new_x, current_y + new_y)

#     new_state = deepcopy(game_state)
#     new_state.snake.pop(-1)
#     new_state.snake.insert(0, new_xy)

#     return new_state


# def is_out_of_bounds(game_state: GameSate):
#     x, y = game_state.snake[0]
#     rows, cols = game_state.rows, game_state.cols
#     return x >= cols or x < 0 or y >= rows or y < 0


# def eat(game_state: GameSate, xy: XY):
#     new_state = deepcopy(game_state)
#     new_state.snake.insert(0, xy)
#     return new_state


XY = Tuple[int, int]
Snake = Union[Tuple[Tuple[int, int], ...], List[XY]]
Food = XY


class _direction(NamedTuple):
    NORTH: XY = (0, -1)
    SOUTH: XY = (0, 1)
    WEST: XY = (-1, 0)
    EAST: XY = (1, 0)


Direction = _direction()


def get_snake_head(snake: Snake) -> XY:
    return snake[0]


def move_snake(snake: Snake, direction: XY) -> Snake:
    head = get_snake_head(snake)
    new_head = tuple(sum(i) for i in zip(head, direction))
    return tuple([new_head]) + tuple(snake[:-1])
