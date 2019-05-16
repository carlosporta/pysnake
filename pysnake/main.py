from os import system
from time import sleep
from threading import Thread

from readchar import readchar

from game import (next_action, random_game_state,
                  random_empty_xy, Direction, GameSate)


def draw(state: GameSate):
    for i in range(state.board[0]):
        for j in range(state.board[1]):
            if (j, i) in state.snake:
                print('#', end='')
            elif (j, i) == state.food:
                print('0', end='')
            else:
                print('-', end='')
        print()


def draw_on_thread(stop_drawing, state):
    while not stop_drawing():
        system('cls')
        draw(state())
        sleep(0.5)


def main():
    state = random_game_state((5, 10))
    stop_drawing = False
    drawing_thread = Thread(target=draw_on_thread,
                            args=(lambda: stop_drawing,
                                  lambda: state))
    drawing_thread.start()

    while not stop_drawing:
        key = readchar().decode('utf-8')
        if key is 'q':
            stop_drawing = True
            break
        elif key is 'w':
            state.current_direction = Direction.NORTH
        elif key is 's':
            state.current_direction = Direction.SOUTH
        elif key is 'a':
            state.current_direction = Direction.WEST
        elif key is 'd':
            state.current_direction = Direction.EAST

        function, action = next_action(state.snake,
                                       state.food,
                                       state.current_direction,
                                       state.board)

        if function is not None:
            state.snake = function(state.snake, state.current_direction)
            if action is 'eat':
                state.points += 1
                state.food = random_empty_xy(state.board, snake=state.snake)
        else:
            stop_drawing = True

        state = GameSate(state.board, 0, state.snake, state.food,
                         state.current_direction)


if __name__ == "__main__":
    main()
