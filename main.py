import pygame
from pygame import *
from Utilities.load_image import load_image
from Classes.PyMain import PyMain
from Classes.Player import Player
from Classes.StaticObject import StaticObject

FPS = 30
WIN_WIDTH = 700
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = (0, 0, 0)
HERO_POSITION_X = 300
HERO_POSITION_Y = 300

pygame.init()

hero = Player(HERO_POSITION_X, HERO_POSITION_Y)
locker = StaticObject(200, 200, 24, 'lockerx2.png')

main = PyMain(width=WIN_WIDTH, height=WIN_HEIGHT)
main.add_render_object(locker)

main.mainloop(hero, fps=FPS)  # Главный цикл
