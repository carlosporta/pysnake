from pysnake.gui import create_surface


def size_test(size):
    w, h = size

    info_size = (round(0.3 * w), h)
    info = create_surface(info_size)
    assert info.get_size() == info_size

    game_size = (round(0.7 * w), h)
    game = create_surface(game_size)
    assert game.get_size() == game_size

    assert info.get_size()[0] + game.get_size()[0] == w


def test_canvas_layout_size():
    sizes = [[256, 144], [1280, 720], [1920, 1080]]
    [size_test(size) for size in sizes]
