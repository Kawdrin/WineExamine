from pygame.sprite import Sprite
from pygame import Rect, mouse, Surface
from pygame.transform import scale
from tools.sprite_sheet import SpriteSheet

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
