from pygame.sprite import Sprite
from pygame import Rect
from pygame.transform import scale
from tools.sprite_sheet import SpriteSheet

SPRITESHEET = SpriteSheet('res/wine.png')

class JanelaDetalhe(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.image = SPRITESHEET.corta_sprite(272, 16, 16*7, 16*5)
        self.image = scale(self.image, [16*7*4, 16*5*4])
        self.rect = Rect(0,0,16*7*4, 16*5*4)

    def update(self):
        ...
