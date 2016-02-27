import pygame
import os
import sys
from pgu import gui
from Utilities.sorting import *
from Classes.Camera import Camera
from Utilities.map_loader import map_loader

FPS = 40
BACKGROUND_COLOR = (0, 0, 0)
WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (800, 600)


# Пока не используется
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                            # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)    # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)                            # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)


screen = pygame.display.set_mode((600, 600))
screen.fill(pygame.Color(0, 0, 0))
rect_pgu = pygame.Rect(50, 50, 300, 100)

btn_click = gui.Button("Click Me")
btn_ok = gui.Button("Ok")
data = [
        ('File/Save', None, None),
        ('File/New', None, None),
        ('Edit/Copy', None, None),
        ('Edit/Cut', None, None),
        ('Help/About', None, None),
        ('Help/Reference', None, None),
        ]
menu = gui.Menus(data)

table = gui.Table()
table.td(menu)
table.tr()
table.td(btn_click)
table.tr()
table.td(btn_ok)

app = gui.App()

app.init(widget=table, screen=screen, area=rect_pgu)


render_list = []
none_render_list = []
clock = pygame.time.Clock()

# camera = Camera(camera_configure, total_level_width, total_level_height)

while True:
    for e in pygame.event.get():
        for obj in render_list:
            obj.event(e)
        for obj in none_render_list:
            obj.event(e)
        if e.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

    dt = clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)
    app.paint()

    for obj in render_list:
        obj.update(dt)

    sort_by_y(render_list)

    for obj in render_list:
        obj.render(screen)
