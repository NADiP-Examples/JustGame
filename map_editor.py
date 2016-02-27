import pygame
import tkinter as tk
from tkinter import *
import os
import platform
from Utilities.sorting import *
from Classes.Camera import Camera

FPS = 40
BACKGROUND_COLOR = (0, 0, 0)
WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (800, 600)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                            # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)    # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)                            # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)


root = tk.Tk()


def destr():
    root.destroy()


but = tk.Button(root, text="OK", command=destr)
but.pack(side=BOTTOM)
root.mainloop()

root = tk.Tk()

embed = tk.Frame(root, width=800, height=600)
embed.grid(columnspan=2000, rowspan=600)  # Adds grid
embed.pack(side=LEFT)  # packs window to the left

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
if platform == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((2000, 600))
screen.fill(pygame.Color(0, 0, 0))
pygame.display.init()
pygame.display.update()

menubar = Menu(root)


def hello():
    # Заглушка
    print("hello!")


# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# display the menu
root.config(menu=menubar)

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

    root.update()
    pygame.display.update()

    dt = clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)

    for obj in render_list:
        obj.update(dt)

    sort_by_y(render_list)

    for obj in render_list:
        obj.render(screen)
