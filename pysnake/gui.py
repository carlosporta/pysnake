from dataclasses import dataclass, field
from typing import Tuple

from pygame import Surface
from pygame.font import SysFont


RGB = Tuple[int, int, int]

_base_size = [256, 144]

@dataclass
class Font:
    BIG: SysFont
    SMALL: SysFont


def create_font(surface_size):
    w, h = surface_size

SysFont(None, 20)
SysFont(None, 13)


@dataclass
class Color:
    DARK_GREY: RGB = field(default=(30, 30, 30))
    LIGHT_GREY: RGB = field(default=(140, 140, 140))
    WHITE: RGB = field(default=(255, 255, 255))
    RED: RGB = field(default=(255, 0, 0))


@dataclass
class GameCanvas:
    root: Surface
    info: Surface
    game: Surface


# def start(screen_size):
#     def start_pygame(size):
#     pygame.init()
#     pygame.display.set_caption('Snake')
#     screen = pygame.display.set_mode(size)
#     info = pygame.Surface((400, 600))
#     game = pygame.Surface((400, 600))
#     return GameCanvas(screen, info, game)

def create_surface(size) -> Surface:
    return Surface(size)
