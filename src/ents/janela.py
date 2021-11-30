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

class VinhosMask(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((16*5*4,16*3*4))
        self.image.fill((204,108,82, 25))
        self.rect = Rect(16*4, 16*6*4, 16*5*4, 16*3*4)

    def update(self, evento, vinho=None):
        ...

    def pressionar(self):
        ...

    def click(self):
        return ['----', '', '', '', '', '', '']


class Vinho(Sprite):
    locate_x = 16*4
    locate_y = 16*6*4
    sprites = {"Rosé":SPRITESHEET.corta_sprite(128, 208,16,16),
               "Tinto":SPRITESHEET.corta_sprite(144, 208,16,16),
               "Espumante":SPRITESHEET.corta_sprite(160, 208,16,16),
               "Frisante":SPRITESHEET.corta_sprite(160, 208,16,16),
               "Licoroso":SPRITESHEET.corta_sprite(112, 208,16,16),
               "Branco":SPRITESHEET.corta_sprite(176, 208,16,16)}

    sprite_click = {"Rosé":SPRITESHEET.corta_sprite(128, 224,16,16),
               "Tinto":SPRITESHEET.corta_sprite(144, 224,16,16),
               "Espumante":SPRITESHEET.corta_sprite(160, 224,16,16),
               "Frisante":SPRITESHEET.corta_sprite(160, 224,16,16),
               "Licoroso":SPRITESHEET.corta_sprite(112, 224,16,16),
               "Branco":SPRITESHEET.corta_sprite(176, 224,16,16)}

    botap_pressionado = None

    @classmethod
    def ajustar_locates(cls):
        cls.locate_x += 16*4
        if cls.locate_x >= 16*4*6:
            cls.locate_x = (cls.locate_x/6)
            cls.locate_y += 16*4

    def __init__(self, dados_vinho,  *groups):
        super().__init__(*groups)
        global SPRITESHEET
        self.loc_y = self.locate_y
        self.dados_vinho = dados_vinho
        self.nao_pressionado()
        self.pressionar = self.pressionado
        self.rect = Rect(self.locate_x, self.locate_y, 16*4, 16*4)
        self.ajustar_locates()

    def pressionado(self):
        self.image = self.sprite_click[self.dados_vinho[1]]
        self.image = scale(self.image, (16*4, 16*4))
        self.pressionar = self.nao_pressionado

    def nao_pressionado(self):
        self.image = self.sprites[self.dados_vinho[1]]
        self.image = scale(self.image, (16*4, 16*4))
        self.pressionar = self.pressionado

    def update(self, evento, reflesh = False):
        if reflesh:
            self.rect.y = self.loc_y
        else:
            self.rect.y += evento*8

    def click(self):
        self.pressionar()
        return self.dados_vinho

class ListaVinhos(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((16*5*4,16*3*4))
        self.image.fill((204,108,82))
        self.rect = Rect(16*4, 16*5*4, 16*4*4, 16*4*4)

    def update(self):
        ...
