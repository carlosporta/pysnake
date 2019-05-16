from os import system
from time import sleep
from threading import Thread

from readchar import readchar

from game import (calculate_new_XY, move, eat, next_action, random_game_state,
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
    print(state.points)


def draw_on_thread(stop_drawing, state):
    while not stop_drawing():
        system('cls')
        draw(state())
        sleep(0.1)


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

        action = next_action(state.snake,
                             state.food,
                             state.current_direction,
                             state.board)

        if action is 'eat':
            eat_pos = calculate_new_XY(state.snake[0], state.current_direction)
            state.snake = eat(state.snake, eat_pos)
            state.points += 1
            state.food = random_empty_xy(state.board, snake=state.snake)
        elif action is 'move':
            state.snake = move(state.snake, state.current_direction)
        else:
            stop_drawing = True


if __name__ == "__main__":
    main()
