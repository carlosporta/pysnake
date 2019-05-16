from dataclasses import dataclass
from random import randint, choice
from typing import NamedTuple, Tuple


# Data types
XY = Tuple[int, int]
Snake = Tuple[XY, ...]
Food = XY
Rows = int
Cols = int
Board = (Rows, Cols)


# Possible directions
class _direction(NamedTuple):
    NORTH: XY = (0, -1)
    SOUTH: XY = (0, 1)
    WEST: XY = (-1, 0)
    EAST: XY = (1, 0)


Direction = _direction()


def random_direction():
    return choice(Direction)


@dataclass
class GameSate:
    board: Board
    points: int
    snake: Snake
    food: Food
    current_direction: XY


def random_game_state(board: Board) -> GameSate:
    snake = (random_empty_xy(board),)
    food = random_empty_xy(board, snake=snake)
    direction = random_direction()
    points = 0
    return GameSate(board, points, snake, food, direction)


# Snake actions
def move(snake: Snake, direction: XY) -> Snake:
    new_head = calculate_new_XY(snake[0], direction)
    new_tail = snake[:-1]
    return (new_head,) + new_tail


def eat(snake: Snake, direction: XY) -> Snake:
    return (direction,) + snake


def next_action(snake: Snake, food: Food, moving_direction: XY, board: Board):
    next_move = calculate_new_XY(snake[0], moving_direction)
    if next_move == food:
        return eat, 'eat'
    elif is_out_of_bounds(next_move, board):
        return None, 'out_of_bounds'
    elif next_move in snake:
        return None, 'self_collision'
    else:
        return move, 'move'


# XY calculcation
def calculate_new_XY(origen: XY, direction: XY) -> XY:
    return tuple(sum(i) for i in zip(origen, direction))


# Board calculus
def is_out_of_bounds(position: XY, board: Board):
    # i is the lower bound = -1
    # j is the x and y values
    # k is the upper bound, rows and cols
    return not(all(i < j < k for i, j, k in zip((-1, -1), position, board)))


# Random board calculus
def random_xy(board: Board) -> XY:
    return (randint(0, board[1] - 1), randint(0, board[0] - 1))


def random_empty_xy(board: Board,
                    snake: Snake = [],
                    food: Food = []) -> XY:
    if len(snake) == board[0] * board[1]:
        return None

    # TODO refactor
    while True:
        xy = random_xy(board)
        if xy == food or xy not in snake:
            return xy
