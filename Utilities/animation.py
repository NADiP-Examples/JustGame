from pygame import *


class Animation:
    def __init__(self, sprites=None, time=100):
        self.sprites = sprites
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

    def update(self, dt):
        self.work_time += dt
        # Считаем сколько кадров надо перелистнуть
        self.skip_frame = self.work_time / self.time
        if self.skip_frame > 0:
            # Не забываем, что у нас, при смене кадров с частотой в
            # 100 мс, вполне могло уже пройти 133 мс, и важно не
            # забыть про эти 33 мс.
            self.work_time %= self.time
            self.frame += int(self.skip_frame)
            if type(self.sprites) == list:
                if self.frame >= len(self.sprites):
                    self.frame = 0

    def get_sprite(self):
        if type(self.sprites) == list:
            return self.sprites[self.frame]
        else:
            return self.sprites
