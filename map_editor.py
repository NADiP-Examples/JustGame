import pygame
import os
import sys
import json
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


# Загрузка и обработка json-карты
f = open(os.path.join('Maps', 'test_map.json'))

map = json.loads(f.read())

f2 = open(os.path.join('Descriptions', 'objects.json'))
obj_descr = json.loads(f2.read())

objs, back, start_pos = map_loader(map, obj_descr)

f.close()
f2.close()


screen = pygame.display.set_mode((600, 600))
screen.fill(pygame.Color(0, 0, 0))


rect_pgu = pygame.Rect(0, 0, 300, 100)

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
app = gui.App()
app.init(widget=table, screen=screen, area=rect_pgu)


render_list = objs  # Список словарей с объектами и их функциями (если нет функции - None)
none_render_list = []
clock = pygame.time.Clock()

# camera = Camera(camera_configure, total_level_width, total_level_height)


while True:
    for e in pygame.event.get():
        app.event(e)
        for obj in render_list:
            obj["object"].event(e)
        for obj in none_render_list:
            obj.event(e)
        if e.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

    dt = clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)

    for obj in render_list:
        obj["object"].update(dt)

    sort_by_y(render_list)

    for obj in render_list:
        obj["object"].render(screen)

    app.paint()
    pygame.display.flip()
