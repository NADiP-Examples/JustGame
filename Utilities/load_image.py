from pygame import *
import os

init()


def load_image(name, path='Pictures', alpha_channel=False):
    pictures = []

    if type(name) == list:
        for n in name:
            fullname = os.path.join(path, n)

            try:
                picture = image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
            except error:  # Если картинки нет на месте
                print("Cannot load image:", n)
                return 0

            w = 2
            h = 2
            surface = display.set_mode((w, h))

            if alpha_channel:
                picture.convert_alpha()
            else:
                picture.convert()

            pictures.append(picture)

        return pictures

    else:
        fullname = os.path.join(path, name)
        try:
            picture = image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
        except error:  # Если картинки нет на месте
            print("Cannot load image:", name)
            return 0

        if alpha_channel:
            picture.convert_alpha()
        else:
            picture.convert()

        return picture

if __name__ == '__main__':
    w = 640
    h = 480
    surface = pygame.display.set_mode((w, h))
