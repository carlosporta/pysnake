from os import system, name

from readchar import readchar

from game import (change_snake_direction, snake_head, snake_tail,
                  Directions, next_state, random_state, State)


def _clear():
    def win_cls():
        system('cls')

    def posix_clear():
        system('clear')

    if name is 'nt':
        return win_cls
    else:
        return posix_clear


clear = _clear()


def draw(state: State) -> None:
    clear()
    print(f'Points: {state.points}/{(state.rows * state.cols) - 1}\n')
    border = ''.join('/' for i in range(state.cols))
    print(border)
    for i in range(state.rows):
        for j in range(state.cols):
            if (i, j) == snake_head(state):
                print('@', end='')
            elif (len(snake_tail(state)) > 0 and
                  (i, j) == snake_tail(state)[-1]):
                print('-', end='')
            elif (i, j) in state.snake.body:
                print('#', end='')
            elif (i, j) == state.food:
                print('.', end='')
            else:
                print(' ', end='')
        print('|')
    print(border)


def main():
    rows = 6
    cols = 10
    state = random_state(rows, cols)
    draw(state)
    key = ''
    while state and key != 'q' and state.points < (rows * cols) - 1:
        key = readchar()
        if key == 'w':
            state = change_snake_direction(Directions.NORTH, state)
        elif key == 's':
            state = change_snake_direction(Directions.SOUTH, state)
        elif key == 'd':
            state = change_snake_direction(Directions.EAST, state)
        elif key == 'a':
            state = change_snake_direction(Directions.WEST, state)

        state = next_state(state)
        if state:
            draw(state)


if __name__ == "__main__":
    main()
