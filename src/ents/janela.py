from pygame.sprite import Sprite
from pygame import Rect, mouse, Surface
from pygame.transform import scale
from tools.sprite_sheet import SpriteSheet
import sqlite3

SPRITESHEET = SpriteSheet('res/wine.png')

class Mouse(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((4,4))
        self.rect = Rect(0,0,4,4)

    def update(self):
        self.rect.x, self.rect.y = mouse.get_pos()


class JanelaDetalhe(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.image = SPRITESHEET.corta_sprite(272, 16, 16*7, 16*5)
        self.image = scale(self.image, [16*7*4, 16*5*4])
        self.rect = Rect(0,0,16*7*4, 16*5*4)

    def update(self):
        ...

class JanelaVinhos(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.image = SPRITESHEET.corta_sprite(16, 96, 16*7, 16*5)
        self.image = scale(self.image, [16*7*4, 16*5*4])
        self.rect = Rect(0,16*5*4,16*7*4, 16*5*4)

    def update(self):
        ...

class Vinho(Sprite):
    locate_x = 16*4
    locate_y = 16*6*4

    @classmethod
    def ajustar_locates(cls):
        cls.locate_x += 16*4
        if cls.locate_x >= 16*4*6:
            cls.locate_x = (cls.locate_x/6)
            cls.locate_y += 16*4

    def __init__(self, *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.image = SPRITESHEET.corta_sprite(128, 208,16,16)
        self.image = scale(self.image, (16*4, 16*4))
        self.rect = Rect(self.locate_x, self.locate_y, 16*4, 16*4)
        self.ajustar_locates()

    def update(self, evento):
        self.rect.y += evento*8

class ListaVinhos(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((16*5*4,16*3*4))
        self.image.fill((204,108,82))
        self.rect = Rect(16*4, 16*6*4, 16*5*4, 16*3*4)

    def update(self):
        ...
