from pygame import *
from Utilities.load_image import load_image


class StaticObject(sprite.Sprite):
    def __init__(self, x, y, height, picture):
        sprite.Sprite.__init__(self)
        self.image = load_image(picture)
        self.rect = Rect(x, y, self.image.get_rect().width, height)

    def update(self, dt):
        pass

    def event(self, e):
        pass

    def render(self, screen):
        y = self.rect.y - self.image.get_rect().height + self.rect.height
        screen.blit(self.image, (self.rect.x, y))
