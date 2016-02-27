import sys
import pygame
from Classes.PyMain import PyMain
# from pygame import *

from Utilities.load_image import load_image


class SuperPyMain(PyMain):
    def mainloop(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                for obj in self.render_list:
                    obj.event(event)
                for obj in self.none_render_list:
                    obj.event(event)
                if event.type == pygame.QUIT:
                    sys.exit()
            dt = clock.tick(40)
            self.screen.fill((0, 0, 0))
            for render_obj in self.render_list:
                render_obj.render(self.screen)
                render_obj.update(dt)

            pygame.display.flip()


class DemoCursor:
    def __init__(self):
        self.image = load_image('locker.png', path='../Pictures/', alpha_channel=True)
        self.rect = self.image.get_rect()

    def event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            self.rect.center = event.pos

    def update(self, pos):
        # self.rect.move(*pos)
        pass

    def render(self, screen):
        screen.blit(self.image, self.rect)


if __name__ == "__main__":
    window = SuperPyMain()
    obj = DemoCursor()
    window.add_render_object(obj)
    window.mainloop()
