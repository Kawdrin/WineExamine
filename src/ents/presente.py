from pygame.sprite import Sprite
from pygame import Rect
from pygame import display
from pygame.transform import scale
from tools.sprite_sheet import SpriteSheet

SPRITESHEET = SpriteSheet('res/wine.png')

class PresenteFechado(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.groups = groups
        self.aberto = False
        self.image = SPRITESHEET.corta_sprite(272,112,16*3+2,16*3+2)
        self.image = scale(self.image, [16*3*4+4, 16*3*4+4])
        self.rect = Rect(16*2*4, 16*4, 16*3*4, 16*3*4)

    def update(self):
        ...
    def click(self):
        self.kill()
        display.set_mode([16*7*4, 16*10*4])
        self = PresenteAberto(self.groups)

class PresenteAberto(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.aberto = True
        self.image =  SPRITESHEET.corta_sprite(208,208,16*6, 16*4)
        self.image = scale(self.image, [16*6*4, 16*4*4])
        self.rect = Rect(16*4/2, 16*4/2+4,16*6*4, 16*4*4)

    def update(self):
        ...

    def click(self):
        ...
