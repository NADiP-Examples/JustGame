from pygame import *
from Utilities.load_image import load_image


class StaticObject(sprite.Sprite):
    def __init__(self, x, y,  picture, height=False):
        sprite.Sprite.__init__(self)
        self.image = load_image(picture, alpha_channel=True)
        if height:
            self.rect = Rect(x, y, self.image.get_rect().width, height)
        else:
            self.rect = False
            self.pos = (x, y)

    def update(self, dt):
        pass

    def event(self, e):
        pass

    def render(self, screen):
        if self.rect:
            y = self.rect.y - self.image.get_rect().height + self.rect.height
            screen.blit(self.image, (self.rect.x, y))
        else:
            screen.blit(self.image, self.pos)
