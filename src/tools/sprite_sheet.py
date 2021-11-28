import pygame
from pygame import Surface, image

class SpriteSheet:
    def __init__(self, imagem_sprite_Sheet):
        self.img = image.load(imagem_sprite_Sheet)

    def corta_sprite(self, x, y, largura, altura):
        sprite = Surface((largura, altura), pygame.SRCALPHA)
        sprite.blit(self.img, (0,0), (x,y,largura,altura))
        return sprite
