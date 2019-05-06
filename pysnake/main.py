from dataclasses import dataclass
from random import randint

import pygame
# from game import move_snake

# from game import random_game_state, is_out_of_bounds, keep_going, move, eat, Direction, GameSate


@dataclass
class GameCanvas:
    root: pygame.Surface
    info: pygame.Surface
    game: pygame.Surface


DARK_GREY = (30, 30, 30)
LIGHT_GREY = (140, 140, 140)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def random_rgb():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def start_pygame(size):
    pygame.init()
    pygame.display.set_caption('Snake')
    screen = pygame.display.set_mode(size)
    info = pygame.Surface((400, 600))
    game = pygame.Surface((400, 600))
    return GameCanvas(screen, info, game)


def draw_info(screen, info, points):
    big_font = pygame.font.SysFont(None, 20)
    small_font = pygame.font.SysFont(None, 13)
    exit_text = small_font.render('Press q to exit', True, WHITE)
    restart_text = small_font.render('Press r to restart', True, WHITE)
    points_text = big_font.render(f'Points: {points}', True, WHITE)
    info.fill(DARK_GREY)
    info.blit(exit_text, (20, 10))
    info.blit(restart_text, (20, 30))
    info.blit(points_text, (20, 80))
    pygame.draw.line(info, WHITE, (0, 60), (400, 60))


# def draw_game(game_screen: pygame.Surface, game_state: GameSate):
def draw_game(game_screen: pygame.Surface, game_state):
    game_screen.fill(DARK_GREY)
    for y in range(game_state.rows):
        for x in range(game_state.cols):
            if (x, y) == game_state.food:
                pygame.draw.rect(game_screen, LIGHT_GREY, (x * 10, y * 10, 10, 10))
                pygame.draw.rect(game_screen, RED, (x * 10+1, y * 10+1, 8, 8))
            elif (x, y) in game_state.snake:
                pygame.draw.rect(game_screen, LIGHT_GREY, (x * 10, y * 10, 10, 10))
                pygame.draw.rect(game_screen, WHITE, (x * 10+1, y * 10+1, 8, 8))


def draw(game_canvas, game_state):
    draw_info(game_canvas.root, game_canvas.info, 10)
    # draw_info(game_canvas.root, game_canvas.info, game_state.points)
    # draw_game(game_canvas.game, game_state)
    game_canvas.root.blit(game_canvas.info, (0, 0))
    # game_canvas.root.blit(game_canvas.game, (400, 0))
    pygame.draw.line(game_canvas.root, WHITE, (400, 0), (400, 600))


# def game_loop(game_canvas: GameCanvas, game_state: GameSate):
def game_loop(game_canvas: GameCanvas, game_state):
    done = False
    # game_state = keep_going(game_state)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            # elif event.key == pygame.K_UP:
                # game_state = move(game_state, Direction.NORTH)
            # elif event.key == pygame.K_DOWN:
            #     game_state = move(game_state, Direction.SOUTH)
            # elif event.key == pygame.K_LEFT:
            #     game_state = move(game_state, Direction.WEST)
            # elif event.key == pygame.K_RIGHT:
            #     game_state = move(game_state, Direction.EAST)
        draw(game_canvas, game_state)
    # draw(game_canvas, game_state)
    # done = is_out_of_bounds(game_state)
    return done, game_state


def main():
    screen_size = (256, 144)
    rows, cols = 60, 40

    game_canvas = start_pygame(screen_size)

    # game_state = random_game_state(rows, cols)
    clock = pygame.time.Clock()
    done = False
    while not done:
        # done, game_state = game_loop(game_canvas, game_state)
        done, game_state = game_loop(game_canvas, [])

        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()