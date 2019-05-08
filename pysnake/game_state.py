from dataclasses import dataclass

@dataclass
class GameSate:
    rows: int
    cols: int
    snake: Snake
    food: Food
    points: int
    current_direction: XY


def random_game_state(rows: int, cols: int) -> GameSate:
    game_state = empty_game_state(rows, cols)
    snake = init_snake(random_empty_xy(game_state))
    game_state = add_snake(game_state, snake)
    food = init_food(random_empty_xy(game_state))
    game_state = add_food(game_state, food)
    direction = random_direction()
    game_state = add_direction(game_state, direction)
    return game_state

def empty_game_state(rows: int, cols: int) -> GameSate:
    return GameSate(rows, cols, [], [], 0, [])
