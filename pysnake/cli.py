from os import system, name

from readchar import readchar

from game import (change_snake_direction, Directions,
                  next_state, random_state, State)


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
    for i in range(state.rows):
        for j in range(state.cols):
            if (i, j) in state.snake.body:
                print('#', end='')
            elif (i, j) == state.food:
                print('0', end='')
            else:
                print('-', end='')
        print()


def main():
    state = random_state(2, 2)
    key = ''
    while state and key != 'q':
        draw(state)
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


if __name__ == "__main__":
    main()
