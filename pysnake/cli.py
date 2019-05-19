from os import system

from readchar import readchar

from func import (change_snake_direction, Directions,
                  next_state, random_state, State)


def draw(state: State) -> None:
    system('clear')
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
    state = random_state(6, 10)
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
